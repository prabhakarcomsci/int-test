import requests
import pytest
import json

@pytest.fixture
def create_post():
    user = {
        "userId": 1234,
        "body": "new request body",
        "title": "New fixture User"
    }

    response = requests.post(f"https://jsonplaceholder.typicode.com/posts", json=user)
    print(response.status_code)
    print(response.text)
    return response.json()["id"]


@pytest.mark.parametrize("id", [1, 2, 3])
def test_get_post(id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
    js = response.json()
    print()
    userId = js["userId"]
    id = js["id"]
    title = js["title"]
    body = js["body"]
    print(f"{userId=}, {id=}, {title=}, {body=}")

def test_create_post():
    user = {
        "userId": 123,
        "body": "new request body",
        "title": "New User"
    }

    response = requests.post(f"https://jsonplaceholder.typicode.com/posts", json=user)
    assert response.status_code == 201
    assert response.json()["userId"] == 123

def test_update_post(create_post):
    print(f"UserId: {create_post}")
    id = create_post
    update_user = {
        "id": id,
        "userId": 1234,
        "body": "new request body",
        "title": "Updated User"
    }
    print(update_user)
    response = requests.put(f"https://jsonplaceholder.typicode.com/posts/{id}", json=update_user)
    print(response.status_code)
    print(response.text)
    #assert response.status_code == 201
    #assert response.json()["userId"] == 123

def test_delete_post(create_post):
    id = create_post
    response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{id}")
    assert response.status_code == 200
