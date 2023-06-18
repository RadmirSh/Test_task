import requests
import json

def test_get_request():
    test_url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(test_url)
    print(response.json())
    assert response.status_code == 200

def test_post_request():
    test_url = "https://jsonplaceholder.typicode.com/posts"
    post_1 = {"userId": 1, "title": "Hi People", "id": 101, "body": "main"}
    headers = {"Content-Type": "application/json"}
    response = requests.post(test_url, data=json.dumps(post_1), headers=headers)
    print(response.json())
    # assert response.status_code == 201
    assert response.json() == post_1

def test_delete_request():
    test_url = "https://jsonplaceholder.typicode.com/posts/101"
    response = requests.delete(test_url)
    print(response.json())
    assert response.status_code == 200
    assert  response.json() == {}