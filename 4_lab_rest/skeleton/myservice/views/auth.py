from flask import Blueprint, jsonify, request

auth = Blueprint('auth', __name__)


@auth.route('/auth/pippo', methods=['GET'])
def login():
    json_data = request.get_json()
    email = json_data['email']
    password = json_data['password']
    return jsonify({'email': email})
