#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SASS v5.0 Feedback Loop (FBL) Packet Parser.
"""
import xml.etree.ElementTree as ET
from typing import Dict, Any

class FBLPacketParser:
    @staticmethod
    def parse_xml_packet(xml_string: str) -> Dict[str, Any]:
        root = ET.fromstring(xml_string)
        metadata = root.find("metadata")
        payload = root.find("payload")
        
        meta_dict = {}
        if metadata is not None:
            for child in metadata:
                meta_dict[child.tag] = child.text
                
        payload_dict = {}
        if payload is not None:
            for child in payload:
                payload_dict[child.tag] = child.text

        return {
            "packet_id": meta_dict.get("packet_id", "UNKNOWN"),
            "sender": meta_dict.get("sender_apid", meta_dict.get("sender", "UNKNOWN")),
            "receiver": meta_dict.get("target_apid", meta_dict.get("target", "UNKNOWN")),
            "priority": meta_dict.get("priority", "P1_HIGH"),
            "metadata": meta_dict,
            "payload": payload_dict
        }
