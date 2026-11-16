#!/usr/bin/env bash
# ==============================================================================
# 01_provision_infra.sh — Provision Spanner Enterprise (100 PU), GCS Bucket,
# IAM Binding for Spanner Native Vertex AI Embeddings, and Apply Base Schema
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

ENV_FILE="${ENV_FILE:-${REPO_ROOT}/.env}"
if [[ ! -f "${ENV_FILE}" ]]; then
  echo "[WARN] .env not found at ${ENV_FILE}; falling back to .env.example"
  ENV_FILE="${REPO_ROOT}/.env.example"
fi

set -a
# shellcheck disable=SC1090
source "${ENV_FILE}"
set +a

ACTIVE_LOWER="$(echo "${ACTIVE_ENV:-nonprod}" | tr '[:upper:]' '[:lower:]')"
if [[ "${ACTIVE_LOWER}" == "prod" ]]; then
  PREFIX="PROD_"
else
  PREFIX="NONPROD_"
fi

eval "ENV_NAME=\${${PREFIX}ENVIRONMENT_NAME}"
eval "GCS_BUCKET=\${${PREFIX}GCS_BUCKET}"
eval "GCS_PREFIX=\${${PREFIX}GCS_PREFIX}"
eval "SPANNER_INSTANCE=\${${PREFIX}SPANNER_INSTANCE}"
eval "SPANNER_DISPLAY_NAME=\${${PREFIX}SPANNER_DISPLAY_NAME:-NTT Plant Knowledge Graph}"
eval "SPANNER_DATABASE=\${${PREFIX}SPANNER_DATABASE}"
eval "SPANNER_EDITION=\${${PREFIX}SPANNER_EDITION}"
eval "SPANNER_PU=\${${PREFIX}SPANNER_PROCESSING_UNITS}"

export GOOGLE_CLOUD_QUOTA_PROJECT="${GCP_PROJECT}"

echo "=============================================================================="
echo " NTT Plant Knowledge Graph & Catalog — Infrastructure Provisioning"
echo " Project:          ${GCP_PROJECT}"
echo " Region:           ${GCP_REGION}"
echo " Active Env:       ${ACTIVE_LOWER} (${ENV_NAME})"
echo " GCS Bucket:       gs://${GCS_BUCKET}/${GCS_PREFIX}"
echo " Spanner Instance: ${SPANNER_INSTANCE} (${SPANNER_EDITION}, ${SPANNER_PU} PU)"
echo " Spanner Database: ${SPANNER_DATABASE}"
echo "=============================================================================="

echo "[1/6] Enabling required Google Cloud APIs on ${GCP_PROJECT}..."
gcloud services enable \
  serviceusage.googleapis.com \
  spanner.googleapis.com \
  dataplex.googleapis.com \
  datacatalog.googleapis.com \
  aiplatform.googleapis.com \
  storage.googleapis.com \
  --project="${GCP_PROJECT}"

echo "[2/6] Provisioning Cloud Storage bucket gs://${GCS_BUCKET} in ${GCP_REGION}..."
if ! gcloud storage buckets describe "gs://${GCS_BUCKET}" --project="${GCP_PROJECT}" >/dev/null 2>&1; then
  gcloud storage buckets create "gs://${GCS_BUCKET}" \
    --project="${GCP_PROJECT}" \
    --location="${GCP_REGION}" \
    --uniform-bucket-level-access \
    --public-access-prevention
  gcloud storage buckets update "gs://${GCS_BUCKET}" \
    --project="${GCP_PROJECT}" \
    --update-labels="env=${ENV_NAME},service=${FINOPS_SERVICE:-ntt-kg-demo},owner=${FINOPS_OWNER:-ntt-poc},cost_center=${FINOPS_COST_CENTER:-demo}"
else
  echo "  -> Bucket gs://${GCS_BUCKET} already exists."
fi

echo "[3/6] Syncing okf_bundle Markdown files to gs://${GCS_BUCKET}/${GCS_PREFIX}/..."
gcloud storage rsync --recursive \
  "${REPO_ROOT}/${OKF_BUNDLE_DIR}" \
  "gs://${GCS_BUCKET}/${GCS_PREFIX}" \
  --project="${GCP_PROJECT}"

echo "[4/6] Provisioning Spanner Service Agent & granting Vertex AI User role for native ML.PREDICT..."
gcloud beta services identity create \
  --service=spanner.googleapis.com \
  --project="${GCP_PROJECT}" >/dev/null 2>&1 || true

PROJECT_NUMBER="$(gcloud projects describe "${GCP_PROJECT}" --format='value(projectNumber)')"
SPANNER_SA="service-${PROJECT_NUMBER}@gcp-sa-spanner.iam.gserviceaccount.com"
echo "  -> Granting roles/aiplatform.user to ${SPANNER_SA}..."
gcloud projects add-iam-policy-binding "${GCP_PROJECT}" \
  --member="serviceAccount:${SPANNER_SA}" \
  --role="roles/aiplatform.user" \
  --condition=None \
  --quiet >/dev/null

echo "[5/6] Provisioning Cloud Spanner ${SPANNER_EDITION} instance '${SPANNER_INSTANCE}' (${SPANNER_PU} PU)..."
if ! gcloud spanner instances describe "${SPANNER_INSTANCE}" --project="${GCP_PROJECT}" >/dev/null 2>&1; then
  gcloud spanner instances create "${SPANNER_INSTANCE}" \
    --project="${GCP_PROJECT}" \
    --config="regional-${GCP_REGION}" \
    --description="${SPANNER_DISPLAY_NAME}" \
    --processing-units="${SPANNER_PU}" \
    --edition="${SPANNER_EDITION}" \
    --labels="env=${ENV_NAME},service=${FINOPS_SERVICE:-ntt-kg-demo},owner=${FINOPS_OWNER:-ntt-poc},cost_center=${FINOPS_COST_CENTER:-demo}"
else
  echo "  -> Spanner instance '${SPANNER_INSTANCE}' already exists."
fi

echo "[6/6] Provisioning Spanner database '${SPANNER_DATABASE}' & applying sql/01_schema.sql..."
PYTHON_BIN="${REPO_ROOT}/.venv/bin/python"
if [[ ! -x "${PYTHON_BIN}" ]]; then
  PYTHON_BIN="python3"
fi

if ! gcloud spanner databases describe "${SPANNER_DATABASE}" \
  --instance="${SPANNER_INSTANCE}" \
  --project="${GCP_PROJECT}" >/dev/null 2>&1; then
  gcloud spanner databases create "${SPANNER_DATABASE}" \
    --instance="${SPANNER_INSTANCE}" \
    --project="${GCP_PROJECT}"
  PYTHONPATH="${REPO_ROOT}/src" "${PYTHON_BIN}" "${SCRIPT_DIR}/02_load_spanner.py" --ddl-only
else
  echo "  -> Database '${SPANNER_DATABASE}' exists; ensuring DDL is applied if tables are missing..."
  PYTHONPATH="${REPO_ROOT}/src" "${PYTHON_BIN}" "${SCRIPT_DIR}/02_load_spanner.py" --ddl-if-missing
fi

echo "[DONE] Infrastructure provisioning complete."
