from . import RestForm
from .role import RoleForm
from app.mod_auth.model.group import Group
from wtforms import IntegerField


class GroupForm(RestForm):

    class Meta:
        model = Group

    parent_id = IntegerField("Id do Grupo Pai")
