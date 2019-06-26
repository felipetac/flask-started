from app import DB
from app.mod_auth.model.role import Role as RoleModel, RoleSchema
from app.mod_auth.form.role import RoleForm

class Role():

    def list(self):
        roles = RoleModel.query.all()
        if roles:
            role_schema = RoleSchema(many=True)
            return {"success": True, "result": role_schema.dump(roles)}
        return {"success": False, "result": []}

    def read(self, role_id):
        role = RoleModel.query.filter_by(id=role_id).first()
        if role:
            role_schema = RoleSchema()
            return {"success": True, "result": role_schema.dump(role)}
        return {"success": False, "result": {"id": "Identificador não encontrado!"}}

    def edit(self, json_obj):
        role, flag = RoleModel(), False
        if "id" in json_obj.keys():
            role = RoleModel.query.filter_by(id=json_obj["id"]).first()
            flag = True
        if role:
            form = RoleForm.from_json(request.get_json(), obj=role) # set the object to avoid raising a ValidationError
            if form.validate_on_submit():
                form.populate_obj(role)
                if not flag:
                    DB.session.add(role)
                DB.session.commit()
                role_schema = RoleSchema()
                return {"success": True, "result": role_schema.dump(role)} # Return role with last id insert
            return {"success": False, "result": form.errors}
        return {"success": False, "result": {"id": "Identificador não encontrado!"}}

    def delete(self, role_id):
        role = RoleModel.query.filter_by(id=role_id).first()
        if role:
            DB.session.delete(role)
            DB.session.commit()
            return {"success": True, "result": "Regra apagada com sucesso!"}
        return {"success": False, "result": {"id": "Identificador não encontrado!"}}