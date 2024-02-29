def get_secrets_login():
    from .secrets import secrets_login
    return secrets_login()

def get_secrets_create_users():
    from .secrets import secrets_create_users
    return secrets_create_users()

def get_secrets_list_users():
    from .secrets import secrets_list_users
    return secrets_list_users()

def get_secrets_update_users():
    from .secrets import secrets_update_users
    return secrets_update_users()

def get_secrets_delete_users():
    from .secrets import secrets_delete_users
    return secrets_delete_users()