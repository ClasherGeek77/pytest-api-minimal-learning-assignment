from lib import get_secrets_login
from lib import get_register_users
import pytest

@pytest.fixture(scope="session")
def secrets_login():
    return get_secrets_login()

@pytest.fixture(scope="session")
def register_users():
    return get_register_users()