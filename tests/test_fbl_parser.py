import pytest
from src.fbl_protocol_parser import FBLPacketParser

def test_xml_parsing():
    sample = '''<fbl_packet><metadata><packet_id>TEST-01</packet_id><sender_apid>001-ceo</sender_apid></metadata><payload><status>OK</status></payload></fbl_packet>'''
    res = FBLPacketParser.parse_xml_packet(sample)
    assert res["packet_id"] == "TEST-01"
    assert res["sender"] == "001-ceo"
    assert res["payload"]["status"] == "OK"
