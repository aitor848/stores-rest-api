from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    # Find a user in username_mapping.
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user


def identity(payload):
    # Find a user in id_mapping.
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)