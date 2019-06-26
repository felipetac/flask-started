from flask import request, jsonify
from app.mod_auth.service.group import Group as GroupService
from app.mod_auth.controller import MOD_AUTH

__group = GroupService()

@MOD_AUTH.route('/groups', methods=['GET'])
def list_groups():
    res = __group.list()
    if res["success"]:
        return jsonify(res["result"])
    return jsonify(res["result"]), 204

@MOD_AUTH.route('/group', methods=['POST'])
def create_group():
    res = __group.edit(request.get_json())
    if res["success"]:
        return jsonify(res["result"]), 201
    return jsonify(res["result"]), 406

@MOD_AUTH.route('/group/<int:group_id>', methods=['GET'])
def read_group(group_id):
    res = __group.read(group_id)
    if res["success"]:
        return jsonify(res["result"])
    return jsonify(res["result"]), 204

@MOD_AUTH.route('/group/<int:group_id>', methods=['PUT'])
def update_group(group_id):
    json_obj = request.get_json()
    json_obj["id"] = group_id
    res = __group.edit(json_obj)
    if res["success"]:
        return jsonify(res["result"])
    return jsonify(res["result"]), 406

@MOD_AUTH.route('/group/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
    res = __group.delete(group_id)
    if res["success"]:
        return jsonify(res["result"])
    return jsonify(res["result"]), 406
