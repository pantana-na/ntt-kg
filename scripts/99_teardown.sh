#!/usr/bin/env bash
# ==============================================================================
# 99_teardown.sh — Clean up Spanner Instance, Dataplex Catalog Resources,
# and Optional GCS Bucket to Eliminate Ongoing PoC Charges
# Usage:
#   bash scripts/99_teardown.sh --yes [--delete-bucket]
# ==============================================================================
set -euo pipefail

CONFIRM="false"
DELETE_BUCKET="false"
for arg in "$@"; do
  case "${arg}" in
    --yes) CONFIRM="true" ;;
    --delete-bucket) DELETE_BUCKET="true" ;;
  esac
done

if [[ "${CONFIRM}" != "true" ]]; then
  echo "Refusing to delete cloud resources without --yes."
  echo "Usage: bash scripts/99_teardown.sh --yes [--delete-bucket]"
  exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
ENV_FILE="${ENV_FILE:-${REPO_ROOT}/.env}"
[[ -f "${ENV_FILE}" ]] || ENV_FILE="${REPO_ROOT}/.env.example"

set -a
# shellcheck disable=SC1090
source "${ENV_FILE}"
set +a

ACTIVE_LOWER="$(echo "${ACTIVE_ENV:-nonprod}" | tr '[:upper:]' '[:lower:]')"
PREFIX="NONPROD_"
[[ "${ACTIVE_LOWER}" == "prod" ]] && PREFIX="PROD_"

eval "GCS_BUCKET=\${${PREFIX}GCS_BUCKET}"
eval "SPANNER_INSTANCE=\${${PREFIX}SPANNER_INSTANCE}"
eval "DATAPLEX_ENTRY_GROUP=\${${PREFIX}DATAPLEX_ENTRY_GROUP}"
eval "DATAPLEX_ENTRY_TYPE=\${${PREFIX}DATAPLEX_ENTRY_TYPE}"
eval "DATAPLEX_ASPECT_TYPE=\${${PREFIX}DATAPLEX_ASPECT_TYPE}"

echo "[1/3] Deleting Cloud Spanner instance '${SPANNER_INSTANCE}' in ${GCP_PROJECT}..."
gcloud spanner instances delete "${SPANNER_INSTANCE}" \
  --project="${GCP_PROJECT}" \
  --quiet || echo "  -> Spanner instance already absent."

echo "[2/3] Deleting Dataplex EntryGroup, EntryType, and AspectType in ${DATAPLEX_LOCATION}..."
gcloud dataplex entry-groups delete "${DATAPLEX_ENTRY_GROUP}" \
  --location="${DATAPLEX_LOCATION}" \
  --project="${GCP_PROJECT}" \
  --quiet 2>/dev/null || echo "  -> EntryGroup already absent or entries still draining."

gcloud dataplex entry-types delete "${DATAPLEX_ENTRY_TYPE}" \
  --location="${DATAPLEX_LOCATION}" \
  --project="${GCP_PROJECT}" \
  --quiet 2>/dev/null || true

gcloud dataplex aspect-types delete "${DATAPLEX_ASPECT_TYPE}" \
  --location="${DATAPLEX_LOCATION}" \
  --project="${GCP_PROJECT}" \
  --quiet 2>/dev/null || true

if [[ "${DELETE_BUCKET}" == "true" ]]; then
  echo "[3/3] Deleting GCS bucket gs://${GCS_BUCKET}..."
  gcloud storage rm --recursive "gs://${GCS_BUCKET}" --project="${GCP_PROJECT}" || true
else
  echo "[3/3] Keeping GCS bucket gs://${GCS_BUCKET} (pass --delete-bucket to remove)."
fi

echo "[DONE] Demo teardown complete."
