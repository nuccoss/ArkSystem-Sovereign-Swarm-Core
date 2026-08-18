#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
4-Tier SSoT Parity and CDI (Cognitive Dissociation Index) Inspector.
"""
import hashlib
from typing import Dict, Any

class SSoTParityInspector:
    @staticmethod
    def compute_sha256(content: str) -> str:
        return hashlib.sha256(content.encode("utf-8")).hexdigest()

    @classmethod
    def verify_parity(cls, local_content: str, cloud_content: str) -> Dict[str, Any]:
        local_hash = cls.compute_sha256(local_content)
        cloud_hash = cls.compute_sha256(cloud_content)
        is_equal = local_hash == cloud_hash
        
        return {
            "parity_rate": 100.0 if is_equal else 0.0,
            "local_sha256": local_hash,
            "cloud_sha256": cloud_hash,
            "is_synchronized": is_equal,
            "cdi_metric": 0.0000 if is_equal else 0.5000
        }
