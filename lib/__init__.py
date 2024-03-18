def get_secrets_login():
    from .secrets import secrets_login

    return secrets_login()

def get_register_users():
    from .secrets import register_users

    return  register_users()