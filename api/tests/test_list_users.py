import logging
import requests
import json

def test_list_users_success_reqres():
    url = "https://reqres.in/api/users"
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()
    
    logging.info("API Response: ")
    logging.info(response.content.decode("utf-8"))