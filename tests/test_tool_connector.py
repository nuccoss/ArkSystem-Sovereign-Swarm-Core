import pytest
from src.gcs_tool_connector import GCSToolConnector

def test_prefix_validation():
    connector = GCSToolConnector()
    assert connector.validate_prefix("sandbox/layer_0/agent_alpha/README.md") is True
    assert connector.validate_prefix("sandbox/layer_1/node_data/AGENTS.md") is True
    assert connector.validate_prefix("unauthorized_folder/secrets.txt") is False
