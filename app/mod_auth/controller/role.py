from flask import request, jsonify
from werkzeug.datastructures import ImmutableMultiDict
from app.mod_auth.form.role import RoleForm
from app.mod_auth.model.role import Role, RoleSchema
from app.mod_auth.controller import MOD_AUTH
from app import DB


@MOD_AUTH.route('/roles', methods=['GET'])
def list_roles():
    roles = Role.query.all()
    if roles:
        role_schema = RoleSchema(many=True)
        return jsonify(role_schema.dump(roles).data)
    return jsonify("Não há usuários cadastrados na base!"), 204