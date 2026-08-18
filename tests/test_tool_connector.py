import pytest
from src.gcs_tool_connector import GCSToolConnector

def test_prefix_validation():
    connector = GCSToolConnector()
    assert connector.validate_prefix("000_outr_layer/001-ceo/README.md") is True
    assert connector.validate_prefix("100_1st_layer/120-admo/AGENTS.md") is True
    assert connector.validate_prefix("unauthorized_folder/secrets.txt") is False
