"""Spanner SQL DDL template rendering and statement splitting."""

from __future__ import annotations

from pathlib import Path
import re
from typing import List

from .config import DemoSettings


def render_ddl_statements(sql_path: Path, settings: DemoSettings) -> List[str]:
    """Substitute ${VAR} placeholders from DemoSettings and split into clean Spanner DDL statements."""
    raw_sql = sql_path.read_text(encoding="utf-8")
    replacements = {
        "${GCP_PROJECT}": settings.gcp_project,
        "${GCP_REGION}": settings.gcp_region,
        "${GENAI_LOCATION}": settings.genai_location,
        "${EMBEDDING_MODEL}": settings.embedding_model,
        "${EMBEDDING_DIMENSION}": str(settings.embedding_dimension),
        "${SPANNER_DATABASE}": settings.spanner_database,
        "${SPANNER_MODEL_NAME}": settings.spanner_model_name,
        "${SPANNER_GRAPH_NAME}": settings.spanner_graph_name,
    }
    rendered = raw_sql
    for placeholder, val in replacements.items():
        rendered = rendered.replace(placeholder, val)

    unresolved = re.findall(r"\$\{[A-Z0-9_]+\}", rendered)
    if unresolved:
        raise ValueError(f"Unresolved DDL template variables in {sql_path}: {unresolved}")

    # Strip SQL line comments (`-- ...`) and split by `;`
    cleaned_lines = []
    for line in rendered.splitlines():
        stripped = line.strip()
        if stripped.startswith("--"):
            continue
        cleaned_lines.append(line)

    joined = "\n".join(cleaned_lines)
    statements = [stmt.strip() for stmt in joined.split(";") if stmt.strip()]
    return statements
