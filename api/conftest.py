# import sys
# sys.path.append('/path/to/Documents/ClasherGeek77/pytest-api-minimal-learning-assignment/api')
from lib import get_secrets_create_users, get_secrets_delete_users, get_secrets_login, get_secrets_list_users, get_secrets_update_users
import pytest

@pytest.fixture(scope="session")
def secrets_login():
    return get_secrets_login()

@pytest.fixture(scope="session")
def secrets_create_users():
    return get_secrets_create_users()

@pytest.fixture(scope="session")
def secrets_list_users():
    return get_secrets_list_users()

@pytest.fixture(scope="session")
def secrets_update_users():
    return get_secrets_update_users()

@pytest.fixture(scope="session")
def secrets_delete_users():
    return get_secrets_delete_users()