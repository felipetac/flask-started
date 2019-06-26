from flask import request, jsonify
from app.mod_auth.service.role import Role as RoleService
from app.mod_auth.controller import MOD_AUTH

__role = RoleService()

@MOD_AUTH.route('/roles', methods=['GET'])
def list_roles():
    res = __role.list()
    if res["success"]:
        return jsonify(res["result"])
    return jsonify(res["result"]), 204

@MOD_AUTH.route('/role', methods=['POST'])
def create_role():
    res = __role.edit(request.get_json())
    if res["success"]:
        return jsonify(res["result"]), 201
    return jsonify(res["result"]), 406

@MOD_AUTH.route('/role/<int:role_id>', methods=['GET'])
def read_role(role_id):
    res = __role.read(role_id)
    if res["success"]:
        return jsonify(res["result"])
    return jsonify(res["result"]), 204

@MOD_AUTH.route('/role/<int:role_id>', methods=['PUT'])
def update_role(role_id):
    json_obj = request.get_json()
    json_obj["id"] = role_id
    res = __role.edit(json_obj)
    if res["success"]:
        return jsonify(res["result"])
    return jsonify(res["result"]), 406

@MOD_AUTH.route('/role/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    res = __role.delete(role_id)
    if res["success"]:
        return jsonify(res["result"])
    return jsonify(res["result"]), 406
