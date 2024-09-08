import pytest
from jsonschema import validate


# Positive and Negative Test Cases for `/login`

def test_login_success(api_client):
    """Positive Test Case: Login successful."""
    valid_login_data = {"username": "test", "password": "test"}
    response = api_client.post('login', json=valid_login_data)
    assert response.status_code == 200
    assert 'access_token' in response.json()
    # Schema validation
    validate(instance=response.json(), schema={
        "type": "object",
        "properties": {
            "access_token": {"type": "string"}
        },
        "required": ["access_token"]
    })


def test_login_failure(api_client):
    """Negative Test Case: Login with invalid credentials."""
    invalid_login_data = {"username": "wrong", "password": "wrong"}
    response = api_client.post('login', json=invalid_login_data)
    assert response.status_code == 401
    assert response.json().get('message') == "No such username or password"


# Positive and Negative Test Cases for `/test_cases`

def test_get_all_test_cases(api_client_with_auth):
    """Positive Test Case: Get all test cases."""
    response = api_client_with_auth.get('test_cases')
    assert response.status_code == 200
    assert isinstance(response.json().get('test-cases'), list)
    # Schema validation
    validate(instance=response.json(), schema={
        "type": "object",
        "properties": {
            "test-cases": {
                "type": "array",
                "items": {"type": "object"}
            }
        },
        "required": ["test-cases"]
    })


def test_get_test_case_by_id(api_client_with_auth):
    """Positive Test Case: Get a specific test case by ID."""
    test_case_id = 1  # Adjust based on your test data
    response = api_client_with_auth.get(f'test_cases/{test_case_id}')
    assert response.status_code == 200
    assert response.json().get('id') == test_case_id
    # Schema validation
    validate(instance=response.json(), schema={
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "suiteID": {"type": "string"},
            "title": {"type": "string"},
            "description": {"type": "string"}
        },
        "required": ["id", "suiteID", "title", "description"]
    })


def test_add_test_case(api_client_with_auth):
    """Positive Test Case: Add a new test case."""
    test_case_data = {
        "suiteID": "suite_1",
        "title": "New Test Case",
        "description": "Description of the new test case"
    }
    response = api_client_with_auth.post('test_cases', json=test_case_data)
    assert response.status_code == 200
    assert response.json().get('message') == "Test case successfully added"


def test_add_test_case_missing_field(api_client_with_auth):
    """Negative Test Case: Add test case with missing required fields."""
    test_case_data = {
        "suiteID": "suite_1",
        "title": "Incomplete Test Case"
    }
    response = api_client_with_auth.post('test_cases', json=test_case_data)
    assert response.status_code == 400
    assert response.json().get('message') == "Missing request body or required parameter"


def test_delete_all_test_cases(api_client_with_auth):
    """Positive Test Case: Delete all test cases."""
    response = api_client_with_auth.delete('test_cases')
    assert response.status_code == 200
    assert response.json().get('message') == "All test cases successfully deleted"


# Positive and Negative Test Cases for `/test_suites`

def test_get_all_test_suites(api_client_with_auth):
    """Positive Test Case: Get all test suites."""
    response = api_client_with_auth.get('test_suites')
    assert response.status_code == 200
    assert isinstance(response.json().get('test-suites'), list)
    # Schema validation
    validate(instance=response.json(), schema={
        "type": "object",
        "properties": {
            "test-suites": {
                "type": "array",
                "items": {"type": "object"}
            }
        },
        "required": ["test-suites"]
    })


def test_get_test_suite_by_id(api_client_with_auth):
    """Positive Test Case: Get a specific test suite by ID."""
    test_suite_id = 1  # Adjust based on your test data
    response = api_client_with_auth.get(f'test_suites/{test_suite_id}')
    assert response.status_code == 200
    assert response.json().get('id') == test_suite_id
    # Schema validation
    validate(instance=response.json(), schema={
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "length": {"type": "integer"},
            "cases": {"type": "array", "items": {"type": "integer"}}
        },
        "required": ["id", "title", "length", "cases"]
    })


def test_add_test_suite(api_client_with_auth):
    """Positive Test Case: Add a new test suite."""
    test_suite_data = {
        "title": "New Test Suite",
        "length": 1,
        "cases": [1]  # Assume this test case ID exists
    }
    response = api_client_with_auth.post('test_suites', json=test_suite_data)
    assert response.status_code == 200
    assert response.json().get('message') == "Test suite successfully added"


def test_delete_all_test_suites(api_client_with_auth):
    """Positive Test Case: Delete all test suites."""
    response = api_client_with_auth.delete('test_suites')
    assert response.status_code == 200
    assert response.json().get('message') == "All test suites successfully deleted"
