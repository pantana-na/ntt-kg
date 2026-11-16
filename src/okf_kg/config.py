"""Unified multi-environment .env configuration loader (Rule 8 compliant)."""

from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path
from typing import Dict, Mapping, Optional

from dotenv import dotenv_values


@dataclass(frozen=True)
class DemoSettings:
    """Resolved environment configuration for Spanner + Dataplex Demo."""

    active_env: str
    environment_name: str
    gcp_project: str
    gcp_region: str
    genai_location: str
    dataplex_location: str
    dataplex_glossary_location: str
    embedding_model: str
    embedding_dimension: int
    default_model: str
    fast_model: str
    github_repo: str
    artifact_registry_repo: str
    okf_bundle_dir: Path
    gcs_bucket: str
    gcs_prefix: str
    spanner_instance: str
    spanner_display_name: str
    spanner_database: str
    spanner_edition: str
    spanner_processing_units: int
    spanner_model_name: str
    spanner_graph_name: str
    dataplex_entry_group: str
    dataplex_entry_type: str
    dataplex_aspect_type: str
    dataplex_glossary_id: str
    spanner_embed_batch_size: int
    spanner_mutation_batch_size: int
    max_retry_attempts: int
    finops_owner: str
    finops_cost_center: str
    finops_service: str

    @property
    def spanner_model_endpoint(self) -> str:
        return (
            f"//aiplatform.googleapis.com/projects/{self.gcp_project}"
            f"/locations/{self.genai_location}/publishers/google/models/{self.embedding_model}"
        )


def _require_non_empty(raw: Mapping[str, str], key: str) -> str:
    val = (raw.get(key) or "").strip()
    if not val:
        raise ValueError(f"Missing required configuration variable: {key}")
    return val


def load_settings(
    env_file: Optional[Path] = None,
    override_env: Optional[str] = None,
    extra_environ: Optional[Mapping[str, str]] = None,
) -> DemoSettings:
    """Load unified .env settings and resolve NONPROD_* or PROD_* namespace."""
    merged: Dict[str, str] = {}
    if env_file is not None and env_file.exists():
        for k, v in dotenv_values(env_file).items():
            if v is not None:
                merged[k] = v
    elif env_file is None:
        default_env = Path(".env")
        fallback_env = Path(".env.example")
        target = default_env if default_env.exists() else fallback_env
        if target.exists():
            for k, v in dotenv_values(target).items():
                if v is not None:
                    merged[k] = v

    source_env = extra_environ if extra_environ is not None else os.environ
    for k, v in source_env.items():
        if v is not None:
            merged[k] = v

    active = (override_env or merged.get("ACTIVE_ENV") or "nonprod").strip().lower()
    if active not in ("nonprod", "prod"):
        raise ValueError(f"ACTIVE_ENV must be 'nonprod' or 'prod', got: {active!r}")

    prefix = "NONPROD_" if active == "nonprod" else "PROD_"

    gcp_project = _require_non_empty(merged, "GCP_PROJECT")
    gcp_region = _require_non_empty(merged, "GCP_REGION")
    genai_location = (merged.get("GENAI_LOCATION") or gcp_region).strip()
    dataplex_location = (merged.get("DATAPLEX_LOCATION") or gcp_region).strip()
    dataplex_glossary_location = (merged.get("DATAPLEX_GLOSSARY_LOCATION") or "global").strip()

    embedding_dim = int(merged.get("EMBEDDING_DIMENSION") or "768")
    processing_units = int(_require_non_empty(merged, f"{prefix}SPANNER_PROCESSING_UNITS"))
    embed_batch = int(merged.get("SPANNER_EMBED_BATCH_SIZE") or "20")
    mut_batch = int(merged.get("SPANNER_MUTATION_BATCH_SIZE") or "200")
    max_retries = int(merged.get("MAX_RETRY_ATTEMPTS") or "5")

    if embedding_dim <= 0:
        raise ValueError("EMBEDDING_DIMENSION must be positive")
    if processing_units < 100 or processing_units % 100 != 0:
        raise ValueError("SPANNER_PROCESSING_UNITS must be a positive multiple of 100")
    if embed_batch <= 0 or mut_batch <= 0:
        raise ValueError("Batch sizes must be positive integers")

    spanner_display_name = (merged.get(f"{prefix}SPANNER_DISPLAY_NAME") or "NTT Plant Knowledge Graph").strip()
    if not (4 <= len(spanner_display_name) <= 30):
        raise ValueError(
            f"{prefix}SPANNER_DISPLAY_NAME must be 4..30 chars per Spanner API constraint, got {len(spanner_display_name)}: {spanner_display_name!r}"
        )

    return DemoSettings(
        active_env=active,
        environment_name=_require_non_empty(merged, f"{prefix}ENVIRONMENT_NAME"),
        gcp_project=gcp_project,
        gcp_region=gcp_region,
        genai_location=genai_location,
        dataplex_location=dataplex_location,
        dataplex_glossary_location=dataplex_glossary_location,
        embedding_model=_require_non_empty(merged, "EMBEDDING_MODEL"),
        embedding_dimension=embedding_dim,
        default_model=_require_non_empty(merged, "DEFAULT_MODEL"),
        fast_model=_require_non_empty(merged, "FAST_MODEL"),
        github_repo=_require_non_empty(merged, "GITHUB_REPO"),
        artifact_registry_repo=(merged.get("ARTIFACT_REGISTRY_REPO") or "ntt-kg-repo").strip(),
        okf_bundle_dir=Path((merged.get("OKF_BUNDLE_DIR") or "okf_bundle").strip()),
        gcs_bucket=_require_non_empty(merged, f"{prefix}GCS_BUCKET"),
        gcs_prefix=_require_non_empty(merged, f"{prefix}GCS_PREFIX"),
        spanner_instance=_require_non_empty(merged, f"{prefix}SPANNER_INSTANCE"),
        spanner_display_name=spanner_display_name,
        spanner_database=_require_non_empty(merged, f"{prefix}SPANNER_DATABASE"),
        spanner_edition=_require_non_empty(merged, f"{prefix}SPANNER_EDITION"),
        spanner_processing_units=processing_units,
        spanner_model_name=_require_non_empty(merged, f"{prefix}SPANNER_MODEL_NAME"),
        spanner_graph_name=_require_non_empty(merged, f"{prefix}SPANNER_GRAPH_NAME"),
        dataplex_entry_group=_require_non_empty(merged, f"{prefix}DATAPLEX_ENTRY_GROUP"),
        dataplex_entry_type=_require_non_empty(merged, f"{prefix}DATAPLEX_ENTRY_TYPE"),
        dataplex_aspect_type=_require_non_empty(merged, f"{prefix}DATAPLEX_ASPECT_TYPE"),
        dataplex_glossary_id=_require_non_empty(merged, f"{prefix}DATAPLEX_GLOSSARY_ID"),
        spanner_embed_batch_size=embed_batch,
        spanner_mutation_batch_size=mut_batch,
        max_retry_attempts=max_retries,
        finops_owner=(merged.get("FINOPS_OWNER") or "ntt-poc").strip(),
        finops_cost_center=(merged.get("FINOPS_COST_CENTER") or "demo").strip(),
        finops_service=(merged.get("FINOPS_SERVICE") or "ntt-kg-demo").strip(),
    )
