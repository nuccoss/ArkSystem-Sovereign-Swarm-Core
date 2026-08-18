#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GCAAS Agent Runtime GCS Tool Connector.
Prefix-sandboxed GCS CRUD and Post-Inference Hook.
"""
import os
import time
import json
from typing import Optional, Dict, Any

ALLOWED_PREFIXES = ["000_outr_layer/", "100_1st_layer/", "0000_arksystem_db/", "0001_metacognition_hub/"]

class GCSToolConnector:
    def __init__(self, project_id: Optional[str] = None, bucket_name: str = "arksystem-genesis-data-tokyo"):
        self.project_id = project_id or os.getenv("GCP_PROJECT_ID", "chronolyst-ai-prod-01")
        self.bucket_name = bucket_name
        self._client = None

    @property
    def client(self):
        if self._client is None:
            from google.cloud import storage
            self._client = storage.Client(project=self.project_id)
        return self._client

    def validate_prefix(self, file_path: str) -> bool:
        normalized = file_path.replace("\\", "/").lstrip("/")
        return any(normalized.startswith(prefix) for prefix in ALLOWED_PREFIXES)

    def read_file(self, file_path: str) -> str:
        normalized = file_path.replace("\\", "/").lstrip("/")
        if not self.validate_prefix(normalized):
            raise PermissionError(f"Access denied: '{file_path}' is outside authorized prefixes.")
        bucket = self.client.bucket(self.bucket_name)
        blob = bucket.blob(normalized)
        if not blob.exists():
            raise FileNotFoundError(f"File '{normalized}' does not exist in bucket '{self.bucket_name}'.")
        return blob.download_as_text(encoding="utf-8")

    def write_file(self, file_path: str, content: str) -> str:
        normalized = file_path.replace("\\", "/").lstrip("/")
        if not self.validate_prefix(normalized):
            raise PermissionError(f"Access denied: '{file_path}' is outside authorized prefixes.")
        bucket = self.client.bucket(self.bucket_name)
        blob = bucket.blob(normalized)
        blob.upload_from_string(content, content_type="text/markdown; charset=utf-8")
        return f"SUCCESS: {len(content)} bytes written to 'gs://{self.bucket_name}/{normalized}'"

    def list_files(self, prefix: str) -> list:
        normalized = prefix.replace("\\", "/").lstrip("/")
        if not self.validate_prefix(normalized):
            raise PermissionError(f"Access denied: '{prefix}' is outside authorized prefixes.")
        bucket = self.client.bucket(self.bucket_name)
        blobs = list(self.client.list_blobs(bucket, prefix=normalized))
        return [b.name for b in blobs]

    def post_inference_hook(self, agent_id: str, turn_input: str, turn_output: str, metadata: Optional[Dict[str, Any]] = None) -> str:
        timestamp = int(time.time())
        log_blob_path = f"000_outr_layer/{agent_id}/25_log/{timestamp}_turn.json"
        payload = {
            "agent_id": agent_id,
            "timestamp": timestamp,
            "input": turn_input,
            "output": turn_output,
            "metadata": metadata or {}
        }
        bucket = self.client.bucket(self.bucket_name)
        blob = bucket.blob(log_blob_path)
        blob.upload_from_string(json.dumps(payload, ensure_ascii=False, indent=2), content_type="application/json")
        return f"LOGGED: gs://{self.bucket_name}/{log_blob_path}"
