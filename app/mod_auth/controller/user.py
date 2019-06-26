from flask import request, jsonify
from app.mod_auth.service.user import User as UserService
from app.mod_auth.controller import MOD_AUTH

__user = UserService()

@MOD_AUTH.route('/users', methods=['GET'])
def list_users():
    res = __user.list()
    if res["success"]:
        return jsonify(res["result"])
    return jsonify(res["result"]), 204

@MOD_AUTH.route('/user', methods=['POST'])
def create_user():
    res = __user.edit(request.get_json())
    if res["success"]:
        return jsonify(res["result"]), 201
    return jsonify(res["result"]), 406

@MOD_AUTH.route('/user/<int:user_id>', methods=['GET'])
def read_user(user_id):
    res = __user.read(user_id)
    if res["success"]:
        return jsonify(res["result"])
    return jsonify(res["result"]), 204

@MOD_AUTH.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    json_obj = request.get_json()
    json_obj["id"] = user_id
    res = __user.edit(json_obj)
    if res["success"]:
        return jsonify(res["result"])
    return jsonify(res["result"]), 406

@MOD_AUTH.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    res = __user.delete(user_id)
    if res["success"]:
        return jsonify(res["result"])
    return jsonify(res["result"]), 406
