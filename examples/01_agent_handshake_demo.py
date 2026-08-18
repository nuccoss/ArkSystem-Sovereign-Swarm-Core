import os
import sys

# Ensure repository root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.fbl_protocol_parser import FBLPacketParser
from src.ssot_parity_inspector import SSoTParityInspector

SAMPLE_FBL = '''<?xml version="1.0" encoding="UTF-8"?>
<fbl_packet version="5.0">
  <metadata>
    <packet_id>FBL-DEMO-001</packet_id>
    <sender_apid>agent-orchestrator-alpha</sender_apid>
    <target_apid>agent-executor-beta</target_apid>
    <priority>P0_CRITICAL</priority>
  </metadata>
  <payload>
    <command>EXECUTE_SANDBOX_AUDIT</command>
    <status>ACTIVE</status>
  </payload>
</fbl_packet>'''

def main():
    print("=== SASS v5.0 Multi-Agent FBL Handshake Demo ===")
    parsed = FBLPacketParser.parse_xml_packet(SAMPLE_FBL)
    print(f"Packet ID : {parsed['packet_id']}")
    print(f"Sender    : {parsed['sender']}")
    print(f"Receiver  : {parsed['receiver']}")
    print(f"Priority  : {parsed['priority']}")
    
    # Parity verification
    parity = SSoTParityInspector.verify_parity(SAMPLE_FBL, SAMPLE_FBL)
    print(f"SSoT Parity: {parity['parity_rate']}% (CDI: {parity['cdi_metric']})")
    print("=== Handshake Completed Successfully! ===")

if __name__ == "__main__":
    main()
