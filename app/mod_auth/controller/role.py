from flask import request, jsonify
from app.mod_auth.service.role import Role as RoleService
from app.mod_auth.controller import MOD_AUTH

@MOD_AUTH.route('/roles', methods=['GET'])
def list_roles():
    res = RoleService.list()
    if res:
        return jsonify(res)
    return jsonify(res), 204

@MOD_AUTH.route('/role', methods=['POST'])
def create_role():
    res = RoleService.edit(request.get_json())
    if res:
        return jsonify(res), 201
    return jsonify("Não foi possível criar a regra."), 406

@MOD_AUTH.route('/role/<int:role_id>', methods=['GET'])
def read_role(role_id):
    res = RoleService.read(role_id)
    if res:
        return jsonify(res)
    return jsonify("Identificador não encontrado."), 406

@MOD_AUTH.route('/role/<int:role_id>', methods=['PUT'])
def update_role(role_id):
    json_obj = request.get_json()
    json_obj["id"] = role_id
    res = RoleService.edit(json_obj)
    if res:
        return jsonify(res)
    return jsonify("Identificador não encontrado."), 406

@MOD_AUTH.route('/role/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    res = RoleService.delete(role_id)
    if res:
        return jsonify("Regra apagada com sucesso.")
    return jsonify("Identificador não encontrado."), 406
