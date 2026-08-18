#!/bin/bash
# Eventarc Trigger Setup Demo for ArkSystem FBL Pipeline

PROJECT_ID="chronolyst-ai-prod-01"
BUCKET_NAME="arksystem-genesis-data-tokyo"
SERVICE_NAME="agent-runtime-fbl-router"
REGION="asia-northeast1"

echo "Creating Eventarc Trigger for GCS FBL Ingestion..."

gcloud eventarc triggers create fbl-router-trigger \
    --project="${PROJECT_ID}" \
    --location="${REGION}" \
    --destination-run-service="${SERVICE_NAME}" \
    --destination-run-region="${REGION}" \
    --event-filters="type=google.cloud.storage.object.v1.finalized" \
    --event-filters="bucket=${BUCKET_NAME}" \
    --service-account="sa-fbl-router@${PROJECT_ID}.iam.gserviceaccount.com"

echo "Trigger configured successfully."
