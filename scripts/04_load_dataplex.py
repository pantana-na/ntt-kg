#!/usr/bin/env python3
"""Populate Google Cloud Dataplex Knowledge Catalog (AspectType, EntryGroup, EntryType, 100 Entries, and Business Glossary)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import random
import sys
import time
from typing import Callable, TypeVar

from google.api_core import exceptions as gcp_exceptions
from google.cloud import dataplex_v1
from google.protobuf import field_mask_pb2

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "src"))

from okf_kg.config import DemoSettings, load_settings
from okf_kg.dataplex_builder import (
    CANONICAL_GLOSSARY_TERMS,
    build_dataplex_entry,
    build_okf_aspect_type,
    build_okf_entry_group,
    build_okf_entry_type,
)
from okf_kg.parser import parse_okf_bundle

T = TypeVar("T")


def _with_backoff(fn: Callable[[], T], max_attempts: int = 5, label: str = "dataplex_rpc") -> T:
    for attempt in range(1, max_attempts + 1):
        try:
            return fn()
        except (
            gcp_exceptions.ResourceExhausted,
            gcp_exceptions.ServiceUnavailable,
            gcp_exceptions.DeadlineExceeded,
        ) as exc:
            if attempt >= max_attempts:
                print(
                    json.dumps(
                        {
                            "status": "UPSTREAM_UNAVAILABLE_DEGRADED",
                            "operation": label,
                            "error": str(exc),
                        }
                    ),
                    file=sys.stderr,
                )
                raise SystemExit(3) from exc
            wait_s = min(30.0, (2 ** (attempt - 1)) + random.uniform(0.1, 0.8))
            print(f"[RETRY] {label} attempt {attempt}/{max_attempts} after {wait_s:.1f}s ({exc})")
            time.sleep(wait_s)
    raise RuntimeError("Unreachable")


def ensure_catalog_schema(client: dataplex_v1.CatalogServiceClient, settings: DemoSettings) -> None:
    parent = f"projects/{settings.gcp_project}/locations/{settings.dataplex_location}"

    # 1. AspectType
    aspect_name = f"{parent}/aspectTypes/{settings.dataplex_aspect_type}"
    aspect_obj = build_okf_aspect_type(settings)
    try:
        client.get_aspect_type(name=aspect_name)
        print(f"[DATAPLEX] AspectType exists: {aspect_name}")
    except gcp_exceptions.NotFound:
        print(f"[DATAPLEX] Creating AspectType: {aspect_name}")
        op = _with_backoff(
            lambda: client.create_aspect_type(
                parent=parent,
                aspect_type_id=settings.dataplex_aspect_type,
                aspect_type=aspect_obj,
            ),
            settings.max_retry_attempts,
            "create_aspect_type",
        )
        op.result(timeout=180)

    # 2. EntryGroup
    group_name = f"{parent}/entryGroups/{settings.dataplex_entry_group}"
    group_obj = build_okf_entry_group(settings)
    try:
        client.get_entry_group(name=group_name)
        print(f"[DATAPLEX] EntryGroup exists: {group_name}")
    except gcp_exceptions.NotFound:
        print(f"[DATAPLEX] Creating EntryGroup: {group_name}")
        op = _with_backoff(
            lambda: client.create_entry_group(
                parent=parent,
                entry_group_id=settings.dataplex_entry_group,
                entry_group=group_obj,
            ),
            settings.max_retry_attempts,
            "create_entry_group",
        )
        op.result(timeout=180)

    # 3. EntryType
    etype_name = f"{parent}/entryTypes/{settings.dataplex_entry_type}"
    etype_obj = build_okf_entry_type(settings)
    try:
        client.get_entry_type(name=etype_name)
        print(f"[DATAPLEX] EntryType exists: {etype_name}")
    except gcp_exceptions.NotFound:
        print(f"[DATAPLEX] Creating EntryType: {etype_name}")
        op = _with_backoff(
            lambda: client.create_entry_type(
                parent=parent,
                entry_type_id=settings.dataplex_entry_type,
                entry_type=etype_obj,
            ),
            settings.max_retry_attempts,
            "create_entry_type",
        )
        op.result(timeout=180)


def seed_business_glossary(
    settings: DemoSettings,
    gclient: dataplex_v1.BusinessGlossaryServiceClient | None = None,
) -> int:
    if gclient is None:
        gclient = dataplex_v1.BusinessGlossaryServiceClient(transport="rest")
    parent = f"projects/{settings.gcp_project}/locations/{settings.dataplex_glossary_location}"
    glossary_name = f"{parent}/glossaries/{settings.dataplex_glossary_id}"

    existing_glossaries = {
        g.name
        for g in _with_backoff(
            lambda: list(gclient.list_glossaries(parent=parent)),
            settings.max_retry_attempts,
            "list_glossaries",
        )
    }
    if glossary_name in existing_glossaries:
        print(f"[GLOSSARY] Glossary exists: {glossary_name}")
    else:
        print(f"[GLOSSARY] Creating Business Glossary: {glossary_name}")
        op = _with_backoff(
            lambda: gclient.create_glossary(
                parent=parent,
                glossary_id=settings.dataplex_glossary_id,
                glossary=dataplex_v1.Glossary(
                    display_name="OKF Plant & Process Safety Glossary",
                    description=(
                        "Canonical nuclear & process safety terminology for Seabrook Station P&IDs, "
                        "Emergency Core Cooling, and IEC 61882 HAZOP / Risk Assessment."
                    ),
                    labels={
                        "env": settings.environment_name,
                        "service": settings.finops_service,
                    },
                ),
            ),
            settings.max_retry_attempts,
            "create_glossary",
        )
        op.result(timeout=180)

    existing_terms = {
        t.name
        for t in _with_backoff(
            lambda: list(gclient.list_glossary_terms(parent=glossary_name)),
            settings.max_retry_attempts,
            "list_glossary_terms",
        )
    }

    seeded = 0
    for term_spec in CANONICAL_GLOSSARY_TERMS:
        term_name = f"{glossary_name}/terms/{term_spec.term_id}"
        if term_name in existing_terms:
            seeded += 1
            continue
        term_obj = dataplex_v1.GlossaryTerm(
            parent=glossary_name,
            display_name=term_spec.display_name,
            description=term_spec.description,
        )
        try:
            res = _with_backoff(
                lambda t=term_spec, obj=term_obj: gclient.create_glossary_term(
                    parent=glossary_name,
                    term_id=t.term_id,
                    term=obj,
                ),
                settings.max_retry_attempts,
                f"create_term:{term_spec.term_id}",
            )
            if hasattr(res, "result"):
                res.result(timeout=120)
            seeded += 1
        except (gcp_exceptions.AlreadyExists, gcp_exceptions.Conflict):
            seeded += 1
    print(f"[GLOSSARY] Verified {seeded} canonical engineering terms in {glossary_name}.")
    return seeded


def upsert_catalog_entries(
    client: dataplex_v1.CatalogServiceClient,
    settings: DemoSettings,
    built_entries: list[tuple[object, dataplex_v1.Entry]],
) -> tuple[int, int]:
    entry_group_parent = (
        f"projects/{settings.gcp_project}/locations/{settings.dataplex_location}"
        f"/entryGroups/{settings.dataplex_entry_group}"
    )
    existing_entries = {
        e.name
        for e in _with_backoff(
            lambda: list(client.list_entries(parent=entry_group_parent)),
            settings.max_retry_attempts,
            "list_entries",
        )
    }

    created_count = 0
    updated_count = 0
    for spec, entry_proto in built_entries:
        entry_id = getattr(spec, "entry_id")
        entry_name = f"{entry_group_parent}/entries/{entry_id}"
        if entry_name in existing_entries:
            entry_proto.name = entry_name
            _with_backoff(
                lambda ep=entry_proto: client.update_entry(
                    request=dataplex_v1.UpdateEntryRequest(
                        entry=ep,
                        update_mask=field_mask_pb2.FieldMask(paths=["entry_source", "aspects"]),
                        allow_missing=True,
                    )
                ),
                settings.max_retry_attempts,
                f"update_entry:{entry_id}",
            )
            updated_count += 1
            continue

        try:
            _with_backoff(
                lambda eid=entry_id, ep=entry_proto: client.create_entry(
                    parent=entry_group_parent,
                    entry_id=eid,
                    entry=ep,
                ),
                settings.max_retry_attempts,
                f"create_entry:{entry_id}",
            )
            created_count += 1
        except (gcp_exceptions.AlreadyExists, gcp_exceptions.Conflict):
            entry_proto.name = entry_name
            _with_backoff(
                lambda ep=entry_proto: client.update_entry(
                    request=dataplex_v1.UpdateEntryRequest(
                        entry=ep,
                        update_mask=field_mask_pb2.FieldMask(paths=["entry_source", "aspects"]),
                        allow_missing=True,
                    )
                ),
                settings.max_retry_attempts,
                f"update_entry:{entry_id}",
            )
            updated_count += 1

    print(
        f"[DATAPLEX] Upserted {len(built_entries)} Knowledge Catalog entries "
        f"(created={created_count}, updated={updated_count})."
    )
    return created_count, updated_count


def main() -> int:
    ap = argparse.ArgumentParser(description="Seed Dataplex Knowledge Catalog with OKF v0.2 entries, aspects, and glossary")
    ap.add_argument("--env-file", type=Path, default=None)
    ap.add_argument("--env", choices=["nonprod", "prod"], default=None)
    ap.add_argument("--skip-glossary", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="Build all protobufs locally without calling GCP APIs")
    args = ap.parse_args()

    settings = load_settings(env_file=args.env_file, override_env=args.env)
    bundle_path = (
        settings.okf_bundle_dir
        if settings.okf_bundle_dir.is_absolute()
        else REPO_ROOT / settings.okf_bundle_dir
    )
    bundle = parse_okf_bundle(
        bundle_dir=bundle_path,
        gcs_bucket=settings.gcs_bucket,
        gcs_prefix=settings.gcs_prefix,
    )

    built_entries = [(spec, build_dataplex_entry(spec, settings)) for spec in bundle.catalog_entries]
    print(
        json.dumps(
            {
                "event": "dataplex_payloads_built",
                "project": settings.gcp_project,
                "location": settings.dataplex_location,
                "entry_group": settings.dataplex_entry_group,
                "aspect_type": settings.dataplex_aspect_type,
                "entries_count": len(built_entries),
                "glossary_terms_count": len(CANONICAL_GLOSSARY_TERMS),
            },
            indent=2,
        )
    )

    if args.dry_run:
        return 0

    client = dataplex_v1.CatalogServiceClient(transport="rest")
    ensure_catalog_schema(client, settings)
    upsert_catalog_entries(client, settings, built_entries)

    if not args.skip_glossary:
        try:
            seed_business_glossary(settings)
        except gcp_exceptions.GoogleAPICallError as exc:
            print(f"[WARN] Business Glossary seeding skipped or unsupported in org policy ({exc})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
