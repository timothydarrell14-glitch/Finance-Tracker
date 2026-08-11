from extensions import db
from utils import get_current_user_id, hash_password, verify_password, create_token
from models.savings import Savings

from flask import request, jsonify

class SavingsController:
    pass