from flask import Blueprint, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from model.user import User
from response_wrapper import success, error
from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token, 
    jwt_required, 
    get_jwt_identity, 
    set_access_cookies, 
    set_refresh_cookies, 
    unset_jwt_cookies
)
auth = Blueprint('user', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return error(400, 'All fields are required')

    user = User.objects(email=email).first()
    if not user:
        return error(404, 'User not registered')

    if not check_password_hash(user.password, password):
        return error(403, 'Incorrect password')

    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    resp = make_response(success(200, {'accessToken': access_token}))
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)
    return resp

@auth.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')

    if not email or not password or not name:
        return error(400, 'All fields are required')

    old_user = User.objects(email=email).first()
    if old_user:
        return error(409, 'User is already registered')

    hashed_password = generate_password_hash(password)
    user = User(email=email, password=hashed_password, name=name)
    user.save()

    return success(201, 'User created successfully')


@auth.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return success(201, {'accessToken': new_access_token})

@auth.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    resp = make_response(success(200, 'User logged out'))
    unset_jwt_cookies(resp)
    return resp
