# import re

from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity

def hash_password(password):
    return generate_password_hash(password)

def verify_password(hashed_password, password):
    return check_password_hash(hashed_password, password)

def create_token(user_id):
    return create_access_token(identity=str(user_id))

def get_current_user_id():
    identity = get_jwt_identity()
    return int(identity) if identity is not None else None

# def check_email_format(email):
#     email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     return re.match(email_regex, email) is not None