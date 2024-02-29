import logging
import requests
import json

def test_delete_users_success_reqres(secrets_delete_users):
    
    url = "https://reqres.in/api/users"
    payload = {
        "email" : secrets_delete_users.name,
        "password" : secrets_delete_users.job
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=payload)
    
    assert response.status_code == 201

    logging.info("API Response: ")
    logging.info(response.content.decode("utf-8"))