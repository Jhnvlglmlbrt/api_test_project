import requests
import pytest

ENDPOINT = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    response = requests.get(f"{ENDPOINT}/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_posts_by_user_id():
    user_id = 1
    response = requests.get(f"{ENDPOINT}/posts", params={"userId": user_id})
    assert response.status_code == 200
    assert all(post["userId"] == user_id for post in response.json())

def test_get_post_by_id():
    post_id = 1
    response = requests.get(f"{ENDPOINT}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id

def test_get_posts_by_title_and_body():
    title = "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    body = "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    response = requests.get(f"{ENDPOINT}/posts", params={"title": title, "body": body})
    assert response.status_code == 200
    assert all(post["title"] == title and post["body"] == body for post in response.json())

def test_create_post_with_required_fields():
    payload = {
        "title": "Test Title",
        "body": "Test Body"
    }
    response = requests.post(f"{ENDPOINT}/posts", json=payload)
    assert response.status_code == 201
    assert "id" in response.json()

def test_create_post_with_all_fields():
    payload = {
        "title": "Test Title",
        "body": "Test Body",
        "userId": 1
    }
    response = requests.post(f"{ENDPOINT}/posts", json=payload)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["userId"] == payload["userId"]

def test_create_post_with_invalid_data():
    payload = {
        "title": "",
        "body": "Test Body"
    }
    response = requests.post(f"{ENDPOINT}/posts", json=payload)
    assert response.status_code == 400

def test_create_post_with_additional_parameters():
    payload = {
        "title": "Test Title",
        "body": "Test Body",
        "userId": 1,
        "extra_param": "Extra"
    }
    response = requests.post(f"{ENDPOINT}/posts", json=payload)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["userId"] == payload["userId"]

def test_delete_existing_post():
    post_id = 1
    response = requests.delete(f"{ENDPOINT}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json() == {}

def test_delete_non_existing_post():
    post_id = 1000
    response = requests.delete(f"{ENDPOINT}/posts/{post_id}")
    assert response.status_code == 404 or response.json() == {}

def test_delete_post_with_invalid_id():
    invalid_id = "abc"
    response = requests.delete(f"{ENDPOINT}/posts/{invalid_id}")
    assert response.status_code == 404 or response.json() == {}

def test_delete_post_with_additional_parameters():
    post_id = 1
    params = {
        "extra_param": "Extra"
    }
    response = requests.delete(f"{ENDPOINT}/posts/{post_id}", params=params)
    assert response.status_code == 200
