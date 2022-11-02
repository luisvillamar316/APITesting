import requests
import json
from IPython import embed
import pytest

headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInBhc3N3b3JkX2hhc2giOiIkMmIkMTIkQS9vRVBVNU5lc3hjM3ozbXJQcTg5dTM4N3RoMy5wOTRsb2trcFd6NS5Ba0ZTWmtpSFV6SUciLCJyb2xlcyI6ImFkbWluIn0.lc0oKbSZSIqTMSgIGy9uwFG-J4tWJVf4bDGU35eic80',
    'Content-Type':'application/json',
    'accept':'application/json'
    
}

    
def test_get_comments():
    response = requests.get(url = 'http://52.221.247.92:8080/comments', headers=headers)
    # embed()
    print(response.text)
    assert response.ok


def test_post_comment():
    url = "http://52.221.247.92:8080/comments/?text="
    comment_id = 'luis'
    payload = ""
    response = requests.request("POST", url+comment_id, headers=headers, data=payload)
    print(response.text)
    assert response.ok


def test_put_comment():
    comment_id = "19"
    comment_text = "hello"
    likes = "123"
    url = 'http://52.221.247.92:8080/comments/'
    response = requests.request("PUT",url+comment_id, data = json.dumps({'comment_text':comment_text, 'likes':likes}), headers=headers)
    # embed()
    print(response.text)
    if response.status_code == 200:
        assert response.ok
    else:
        assert response.text
 
    
def test_delete_comment():
    payload = {}
    comment_id = "19"
    url = 'http://52.221.247.92:8080/comments/'
    response = requests.request("DELETE",url+comment_id, data = payload, headers=headers)
    # embed()
    print(response.content)
    if response.status_code == 200:
        assert response.ok
    else:
        assert response.text

    
def test_get_users():
    payload = {}
    url = 'http://52.221.247.92:8080/users'
    response = requests.request("GET", url,  headers=headers, data=payload)
    # embed()
    print(response.text)
    assert response.ok
   
    
def test_post_users():
    url = "http://52.221.247.92:8080/users"
    username = "luis"
    payload = json.dumps({
          "username": username,
          "password_hash": "string",
          "roles": "user"
        })
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    if response.status_code == 200:
        assert response.ok
    else:
        assert response.text


def test_get_users_me():
    payload = {}
    url = 'http://52.221.247.92:8080/users/me'
    response = requests.request("GET", url,  headers=headers, data=payload)
    # embed()
    print(response.text)
    assert response.ok


def test_delete_users():
    payload = {}
    user_id = "6"
    url = 'http://52.221.247.92:8080/comments/'
    response = requests.request("DELETE",url+user_id, data = payload, headers=headers)
    # embed()
    print(response.content)
    if response.status_code == 200:
        assert response.ok
    else:
        assert response.text


def test_login():
    payload = {"username": "admin", "password": "admin"}
    response = requests.post(url = "http://52.221.247.92:8080/auth/login", data=payload)
    # embed()
    print(response)
    assert response.ok
    
    token = response.json()["access_token"]
    print(token)


def test_get_health():
    response = requests.get(url='http://52.221.247.92:8080/health')
    # embed()
    print(response)
    assert response.ok


if __name__ == "__main__":
    test_get_users()
    test_post_users()
    test_get_users_me()
    test_delete_users()
    test_get_comments()
    test_post_comment()
    test_put_comment()
    test_delete_comment()
    test_login()
    test_get_health()
    

