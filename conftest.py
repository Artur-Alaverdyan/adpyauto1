# tests/conftest.py
import pytest
from src.api_client import APIClient
from jsonschema import validate

BASE_URL = "http://127.0.0.1:5000/api/v1"


@pytest.fixture(scope="session")
def api_client():
    """Fixture to create an APIClient instance."""
    return APIClient(BASE_URL)


@pytest.fixture(scope="session")
def auth_token(api_client):
    """Fixture to get authentication token."""
    response = api_client.post("login", json={"username": "test", "password": "test"})
    return response.json().get("access_token")


@pytest.fixture
def api_client_with_auth(api_client, auth_token):
    """Fixture to create an APIClient instance with authentication token."""
    api_client.auth_token = auth_token
    return api_client
