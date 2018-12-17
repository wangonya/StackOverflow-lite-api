from flask import request, abort, jsonify, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)
users = []


@auth.route('/api/v1/auth/signup', methods=['POST'])
def user_signup():
    # make sure there's data and its properly formatted
    if None or not request.json:
        abort(400)

    username = request.json['username']
    password = request.json['password']

    # check if username already exists to avoid duplicates
    if any(u['username'] == username for u in users):
        return jsonify({'msg': 'username already exists'}), 409

    if 2 > len(username) or 12 < len(username):
        return jsonify({'msg': 'username length invalid'}), 400
    elif 6 > len(password) or 12 < len(password):
        return jsonify({'msg': 'password length invalid'}), 400
    else:
        user = {
            'username': username,
            'password': generate_password_hash(password)
        }
        users.append(user)
        return jsonify({'user': user}), 201


@auth.route('/api/v1/auth/login', methods=['POST'])
def user_login():
    # make sure there's data and its properly formatted
    if None or not request.json:
        abort(400)

    username = request.json['username']
    password = request.json['password']

    if any(u['username'] == username for u in users):
        get_user_password = [u['password'] for u in users if u['username'] == username]
        if check_password_hash(get_user_password[0], password):
            return jsonify({'msg': 'all good'}), 200
        else:
            return jsonify({'msg': 'wrong password'}), 401
    else:
        return jsonify({'msg': 'username does not exist'}), 400
