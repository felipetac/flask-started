from . import RestForm
from .role import RoleForm
from app.mod_auth.model.group import Group
#from wtforms_alchemy import ModelFormField, ModelFieldList
from wtforms.fields import SelectField, SelectMultipleField #, FormField
from app.mod_auth.model.role import Role
from wtforms.validators import Optional

class _ChildForm(RestForm):
    class Meta:
        model = Group

class GroupForm(RestForm):

    class Meta:
        model = Group

    # Utilizar campos abaixo caso queira normalizar
    # o mesmo formulario em várias tabelas (não é o nosso caso)
    #children = ModelFieldList(FormField(_ChildForm))
    #roles = ModelFieldList(FormField(RoleForm))

    parent_id = SelectField('Parent Id', validators=[Optional()], coerce=int)
    roles_id = SelectMultipleField('Roles Ids', validators=[Optional()], coerce=int)