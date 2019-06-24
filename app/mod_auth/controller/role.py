from flask import request, jsonify
from werkzeug.datastructures import ImmutableMultiDict
from app.mod_auth.form.role import RoleForm
from app.mod_auth.model.role import Role, RoleSchema
from app.mod_auth.controller import MOD_AUTH
from app import DB
from app.mod_auth.service.auth import Auth


@MOD_AUTH.route('/roles', methods=['GET'])
@Auth.role("LISTAR_REGRAS")
def list_roles():
    roles = Role.query.all()
    if roles:
        role_schema = RoleSchema(many=True)
        return jsonify(role_schema.dump(roles))
    return jsonify("Não há regras cadastrados na base!"), 204


@MOD_AUTH.route('/role', methods=['POST'])
def create_role():
    form = RoleForm.from_json(request.get_json())
    if form.validate_on_submit():
        role = Role()
        form.populate_obj(role)
        DB.session.add(role)
        DB.session.commit()
        return jsonify("Regra criada com sucesso!")
    return jsonify(form.errors), 406


@MOD_AUTH.route('/role/<int:role_id>', methods=['GET'])
def read_role(role_id):
    role = Role.query.filter_by(id=role_id).first()
    if role:
        role_schema = RoleSchema()
        return jsonify(role_schema.dump(role))
    return jsonify("Não há regras cadastradas na base!"), 204


@MOD_AUTH.route('/role/<int:role_id>', methods=['PUT'])
def update_role(role_id):
    role = Role.query.filter_by(id=role_id).first()
    if role:
        form = RoleForm.from_json(request.get_json(), obj=role) # set the object to avoid raising a ValidationError  
        if form.validate_on_submit():
            form.populate_obj(role)
            DB.session.commit()
            return jsonify("Regra atualizada com sucesso!")
        return jsonify(form.errors), 406
    return jsonify("Id de regra não encontrado!"), 204


@MOD_AUTH.route('/role/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    role = Role.query.filter_by(id=role_id).first()
    if role:
        DB.session.delete(role)
        DB.session.commit()
        return jsonify("Regra apagada com sucesso!")
    return jsonify("Id de regra não encontrado ou já deletado!"), 204
