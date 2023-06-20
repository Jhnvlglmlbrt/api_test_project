import pytest


@pytest.fixture
def endpoint():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def post_id():
    return 1

@pytest.fixture
def user_id():
    return 1

@pytest.fixture
def post_payload():
    return {
        "title": "Test Title",
        "body": "Test Body",
        "userId": 1
    }

@pytest.fixture
def invalid_post_payload():
    return {
        "title": "",
        "body": "Test Body"
    }

@pytest.fixture
def additional_params():
    return {
        "extra_param": "Extra"
    }
