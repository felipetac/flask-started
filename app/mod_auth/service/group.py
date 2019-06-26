from app import DB
from app.mod_auth.model.group import Group as GroupModel, GroupSchema
from app.mod_auth.service.role import Role as RoleService
from app.mod_auth.model.role import RoleSchema
from app.mod_auth.form.group import GroupForm

class Group():

    def list(self):
        groups = GroupModel.query.all()
        if groups:
            group_schema = GroupSchema(many=True)
            return {"success": True, "result": group_schema.dump(groups)}
        return {"success": False, "result": []}

    def read(self, group_id):
        group = GroupModel.query.filter_by(id=group_id).first()
        if group:
            group_schema = GroupSchema()
            return {"success": True, "result": group_schema.dump(group)}
        return {"success": False, "result": {"id": "Identificador não encontrado!"}}

    def edit(self, json_obj):
        group, flag = GroupModel(), False
        if "id" in json_obj.keys(): # if is update
            group = GroupModel.query.filter_by(id=json_obj["id"]).first()
            flag = True
        if group:
            form = GroupForm.from_json(json_obj, obj=group) # set the object to avoid raising a ValidationError  
            groups = self.list()["result"]
            form.parent_id.choices = [(g["id"], g["initials"]) for g in groups]
            role_service = RoleService()
            roles = role_service.list()["result"]
            form.roles_id.choices = [(r["id"], r["name"]) for r in roles]
            if form.validate_on_submit():
                form.populate_obj(group)
                if form.roles_id.data:
                    for role_id in form.roles_id.data:
                        if role_id not in [role.id for role in group.roles]:
                            role = Role.query.filter_by(id=role_id).first()
                            group.roles.append(role)
                if not flag:
                    DB.session.add(group)
                DB.session.commit()
                group_schema = GroupSchema()
                return {"success": True, "result": group_schema.dump(group)} # Return role with last id insert
            return {"success": False, "result": form.errors}
        return {"success": False, "result": {"id": "Identificador não encontrado!"}}

    def delete(group_id):
        group = GroupModel.query.filter_by(id=group_id).first()
        if group:
            DB.session.delete(group)
            DB.session.commit()
            return {"success": True, "result": "Grupo apagado com sucesso!"}
        return {"success": False, "result": {"id": "Identificador não encontrado!"}}