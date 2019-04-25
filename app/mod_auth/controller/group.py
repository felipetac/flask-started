from flask import request, jsonify
from werkzeug.datastructures import ImmutableMultiDict
from app.mod_auth.form.group import GroupForm
from app.mod_auth.model.group import Group, GroupSchema
from app.mod_auth.controller import MOD_AUTH
from app import DB


@MOD_AUTH.route('/groups', methods=['GET'])
def list_groups():
    groups = Group.query.all()
    if groups:
        group_schema = GroupSchema(many=True)
        return jsonify(group_schema.dump(groups).data)
    return jsonify("Não há usuários cadastrados na base!"), 204
