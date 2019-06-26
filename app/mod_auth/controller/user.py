from flask import request, jsonify
from app.mod_auth.service.user import User as UserService
from app.mod_auth.controller import MOD_AUTH

@MOD_AUTH.route('/users', methods=['GET'])
def list_users():
    res = UserService.list()
    if res:
        return jsonify(res)
    return jsonify(res), 204

@MOD_AUTH.route('/user', methods=['POST'])
def create_user():
    res = UserService.edit(request.get_json())
    if res:
        return jsonify(res), 201
    return jsonify("Não foi possível criar o usuário."), 406

@MOD_AUTH.route('/user/<int:user_id>', methods=['GET'])
def read_user(user_id):
    res = UserService.read(user_id)
    if res:
        return jsonify(res)
    return jsonify("Identificador não encontrado."), 406

@MOD_AUTH.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    json_obj = request.get_json()
    json_obj["id"] = user_id
    res = UserService.edit(json_obj)
    if res:
        return jsonify(res)
    return jsonify("Identificador não encontrado."), 406

@MOD_AUTH.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    res = UserService.delete(user_id)
    if res:
        return jsonify("Usuário apagado com sucesso;")
    return jsonify("Identificador não encontrado."), 406
