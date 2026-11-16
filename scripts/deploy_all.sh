#!/usr/bin/env bash
# ==============================================================================
# deploy_all.sh — End-to-End 1-Command Setup for Spanner (Hybrid + Graph)
# and Dataplex Knowledge Catalog Demo in Google Cloud Console
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# 1. Bootstrap Python virtual environment if missing
if [[ ! -x "${REPO_ROOT}/.venv/bin/python" ]]; then
  echo "[SETUP] Creating Python virtual environment at ${REPO_ROOT}/.venv..."
  if command -v uv >/dev/null 2>&1; then
    uv venv --system-site-packages "${REPO_ROOT}/.venv"
    uv pip install --python "${REPO_ROOT}/.venv/bin/python" \
      --default-index https://pypi.org/simple \
      -r "${REPO_ROOT}/requirements.txt"
  else
    python3 -m venv "${REPO_ROOT}/.venv"
    "${REPO_ROOT}/.venv/bin/pip" install --upgrade pip
    "${REPO_ROOT}/.venv/bin/pip" install --index-url https://pypi.org/simple -r "${REPO_ROOT}/requirements.txt"
  fi
fi

PYTHON_BIN="${REPO_ROOT}/.venv/bin/python"
export PYTHONPATH="${REPO_ROOT}/src"

ENV_FILE="${ENV_FILE:-${REPO_ROOT}/.env}"
[[ -f "${ENV_FILE}" ]] || ENV_FILE="${REPO_ROOT}/.env.example"
set -a
# shellcheck disable=SC1090
source "${ENV_FILE}"
set +a
export GOOGLE_CLOUD_QUOTA_PROJECT="${GCP_PROJECT}"

# 2. Provision GCP APIs, GCS Bucket, Spanner Service Agent IAM, & Spanner Enterprise (100 PU)
bash "${SCRIPT_DIR}/01_provision_infra.sh"

# 3. Load 5-Node / 5-Label Property Graph & Hybrid Search Chunks into Spanner
"${PYTHON_BIN}" "${SCRIPT_DIR}/02_load_spanner.py"

# 4. Generate 768-dim Embeddings Natively inside Spanner SQL (ML.PREDICT) + Vector Index
"${PYTHON_BIN}" "${SCRIPT_DIR}/03_embed_spanner.py"

# 5. Populate Dataplex Knowledge Catalog (AspectType, EntryGroup, 100 Entries, Business Glossary)
"${PYTHON_BIN}" "${SCRIPT_DIR}/04_load_dataplex.py"

# 6. Run Live Verification & Print Console Demo Links
echo ""
echo "[VERIFY] Running end-to-end Spanner Hybrid + Graph & Knowledge Catalog verification..."
"${PYTHON_BIN}" "${SCRIPT_DIR}/05_verify_demo.py"
