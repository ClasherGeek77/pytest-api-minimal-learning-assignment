import logging
import requests
import json

def test_login_success_reqres(secrets_login):
    
    url = "https://reqres.in/api/login"
    payload = {
        "email" : secrets_login.email,
        "password" : secrets_login.password
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=payload)
    
    assert response.status_code == 200

    logging.info("API Response: ")
    logging.info(response.content.decode("utf-8"))