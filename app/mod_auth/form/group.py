from . import RestForm
from .user import UserForm
from .role import RoleForm
from app.mod_auth.model.group import Group
from wtforms import IntegerField
from wtforms_alchemy import ModelFieldList, ModelFormField
from wtforms.fields import FormField

class GroupForm(RestForm):

    class Meta:
        model = Group

    parent_id = IntegerField("Id do Grupo Pai")
    users = ModelFieldList(FormField(UserForm))
    roles = ModelFieldList(FormField(RoleForm))
