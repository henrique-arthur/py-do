from flask import Blueprint, jsonify, request
from models.user import User


routes = Blueprint('routes', __name__)

@routes.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify({'Lu': user_id})

@routes.route('/user', methods=['POST'])
def create_user():
    user = request.get_json()
    return jsonify(user), 201

