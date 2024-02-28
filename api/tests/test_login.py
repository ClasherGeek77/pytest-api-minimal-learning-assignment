import requests

def test_login_success_reqres(secrets_login): # secrets_login is a pytest fixture
    url = "https://reqres.in/api/login"
    json_payload = {
        "email": secrets_login.email,
        "password": secrets_login.password
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=json_payload)
    
    assert response.status_code == 200
