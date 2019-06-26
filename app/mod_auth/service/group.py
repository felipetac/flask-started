from app import DB
from app.mod_auth.model.group import Group as GroupModel, GroupSchema
from app.mod_auth.service.role import Role as RoleService
from app.mod_auth.form.group import GroupForm

class Group():

    @staticmethod
    def list():
        groups = GroupModel.query.all()
        if groups:
            group_schema = GroupSchema(many=True)
            return group_schema.dump(groups)
        return []

    @staticmethod
    def read(group_id, serialize=True):
        group = GroupModel.query.filter_by(id=group_id).first()
        if group:
            if serialize:
                group_schema = GroupSchema()
                return group_schema.dump(group)
            return group
        return None

    @classmethod
    def edit(cls, json_obj):
        group, flag = GroupModel(), False
        if "id" in json_obj.keys(): # if is update
            group = cls.read(json_obj["id"])
            flag = True
        if group:
            form = GroupForm.from_json(json_obj, obj=group) # set the object to avoid raising a ValidationError
            form.parent_id.choices = cls.get_choices()
            form.roles_id.choices = RoleService.get_choices()
            if form.validate_on_submit():
                form.populate_obj(group)
                if form.roles_id.data:
                    for role_id in form.roles_id.data:
                        if role_id not in [role.id for role in group.roles]:
                            role = cls.read(role_id, serialize=False)
                            group.roles.append(role)
                if not flag:
                    DB.session.add(group)
                DB.session.commit()
                group_schema = GroupSchema()
                return group_schema.dump(group) # Return role with last id insert
            return {"errors": form.errors}
        return None

    @classmethod
    def delete(cls, group_id):
        group = cls.read(group_id, serialize=False)
        if group:
            DB.session.delete(group)
            DB.session.commit()
            return True
        return None

    @staticmethod
    def get_choices():
        choices = GroupModel.query.with_entities(GroupModel.id, GroupModel.initials)
        if choices:
            group_schema = GroupSchema(many=True, only=('id', 'initials'))
            return [(g["id"], g["initials"]) for g in group_schema.dump(choices)]
        return []