from lib import get_secrets_login
import pytest

@pytest.fixture(scope="session")
def secrets_login():
    return get_secrets_login()