from flask import request, jsonify
from app.mod_auth.service.group import Group as GroupService
from app.mod_auth.controller import MOD_AUTH

@MOD_AUTH.route('/groups', methods=['GET'])
def list_groups():
    res = GroupService.list()
    if res:
        return jsonify(res)
    return jsonify(res), 204

@MOD_AUTH.route('/group', methods=['POST'])
def create_group():
    res = GroupService.edit(request.get_json())
    if res:
        return jsonify(res), 201
    return jsonify("Não foi possível criar o grupo."), 406

@MOD_AUTH.route('/group/<int:group_id>', methods=['GET'])
def read_group(group_id):
    res = GroupService.read(group_id)
    if res:
        return jsonify(res)
    return jsonify("Identificador não encontrado."), 406

@MOD_AUTH.route('/group/<int:group_id>', methods=['PUT'])
def update_group(group_id):
    json_obj = request.get_json()
    json_obj["id"] = group_id
    res = GroupService.edit(json_obj)
    if res:
        return jsonify(res)
    return jsonify("Identificador não encontrado."), 406

@MOD_AUTH.route('/group/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
    res = GroupService.delete(group_id)
    if res["success"]:
        return jsonify("Grupo apagado com sucesso.")
    return jsonify("Identificador não encontrado."), 406
