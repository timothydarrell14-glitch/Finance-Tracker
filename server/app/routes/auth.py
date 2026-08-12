from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__, url_prefix='/authentication')

@auth_bp.post('/login')
def login():
    pass

@auth_bp.post('signup')
def signup():
    pass