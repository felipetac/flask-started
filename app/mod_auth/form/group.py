from . import RestForm
from .role import RoleForm
from app.mod_auth.model.group import Group
from wtforms_alchemy import ModelFormField, ModelFieldList
from wtforms.fields import FormField

class _ChildForm(RestForm):
    class Meta:
        model = Group

class GroupForm(RestForm):

    class Meta:
        model = Group

    children = ModelFieldList(FormField(_ChildForm))
    roles = ModelFieldList(FormField(RoleForm))
