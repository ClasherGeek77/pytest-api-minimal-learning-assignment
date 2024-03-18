import logging
import requests

def test_register_success_reqres(register_users):

    url = "https://reqres.in/api/register"
    payload = {
        "email": register_users.email,
        "password": register_users.password
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=payload)

    assert response.status_code == 200

    logging.info("API response: ")
    logging.info(response.content.decode("utf-8"))