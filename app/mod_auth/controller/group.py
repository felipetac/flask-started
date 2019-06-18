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
    return jsonify("Não há grupos cadastrados na base!"), 204


@MOD_AUTH.route('/group', methods=['POST'])
def create_group():
    form = GroupForm.from_json(request.get_json())
    if form.validate_on_submit():
        group = Group()
        form.populate_obj(group)
        DB.session.add(group)
        DB.session.commit()
        return jsonify("Grupo criado com sucesso!")
    return jsonify(form.errors), 406


@MOD_AUTH.route('/group/<int:group_id>', methods=['GET'])
def read_group(group_id):
    group = Group.query.filter_by(id=group_id).first()
    if group:
        group_schema = GroupSchema()
        return jsonify(group_schema.dump(group))
    return jsonify("Não há grupos cadastrados na base!"), 204


@MOD_AUTH.route('/group/<int:group_id>', methods=['PUT'])
def update_group(group_id):
    group = Group.query.filter_by(id=group_id).first()
    if group:
        form = GroupForm.from_json(request.get_json(), obj=group) # set the object to avoid raising a ValidationError  
        if form.validate_on_submit():
            form.populate_obj(group)
            DB.session.commit()
            return jsonify("Grupo atualizado com sucesso!")
        return jsonify(form.errors), 406
    return jsonify("Id de usuário não encontrado!"), 204


@MOD_AUTH.route('/group/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
    group = Group.query.filter_by(id=group_id).first()
    if group:
        DB.session.delete(group)
        DB.session.commit()
        return jsonify("Grupo apagado com sucesso!")
    return jsonify("Id de usuário não encontrado ou já deletado!"), 204