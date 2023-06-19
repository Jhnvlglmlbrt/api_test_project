import requests
import pytest

ENDPOINT = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def endpoint():
    return ENDPOINT


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


def test_get_posts(endpoint):
    response = requests.get(f"{endpoint}/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_posts_by_user_id(endpoint, user_id):
    response = requests.get(f"{endpoint}/posts", params={"userId": user_id})
    assert response.status_code == 200
    assert all(post["userId"] == user_id for post in response.json())


def test_get_post_by_id(endpoint, post_id):
    response = requests.get(f"{endpoint}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id


def test_get_posts_by_title_and_body(endpoint):
    title = "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    body = "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    response = requests.get(f"{endpoint}/posts", params={"title": title, "body": body})
    assert response.status_code == 200
    assert all(post["title"] == title and post["body"] == body for post in response.json())


def test_create_post_with_required_fields(endpoint, post_payload):
    response = requests.post(f"{endpoint}/posts", json=post_payload)
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_post_with_all_fields(endpoint, post_payload):
    response = requests.post(f"{endpoint}/posts", json=post_payload)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["userId"] == post_payload["userId"]


def test_create_post_with_invalid_data(endpoint, invalid_post_payload):
    response = requests.post(f"{endpoint}/posts", json=invalid_post_payload)
    assert response.status_code == 400


def test_create_post_with_additional_parameters(endpoint, post_payload, additional_params):
    payload = {**post_payload, **additional_params}
    response = requests.post(f"{endpoint}/posts", json=payload)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["userId"] == post_payload["userId"]


def test_delete_existing_post(endpoint, post_id):
    response = requests.delete(f"{endpoint}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json() == {}


def test_delete_non_existing_post(endpoint):
    post_id = 1000
    response = requests.delete(f"{endpoint}/posts/{post_id}")
    assert response.status_code == 404 or response.json() == {}


def test_delete_post_with_invalid_id(endpoint):
    invalid_id = "abc"
    response = requests.delete(f"{endpoint}/posts/{invalid_id}")
    assert response.status_code == 404 or response.json() == {}


def test_delete_post_with_additional_parameters(endpoint, post_id, additional_params):
    response = requests.delete(f"{endpoint}/posts/{post_id}", params=additional_params)
    assert response.status_code == 200
