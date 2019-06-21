from . import RestForm
from app.mod_auth.model.user import User
from wtforms_alchemy import ModelFormField
from wtforms.fields import SelectField
from wtforms.validators import Optional
#from .group import GroupForm


class UserForm(RestForm):

    class Meta:
        model = User

    # Utilizar campos abaixo caso queira normalizar
    # o mesmo formulario em várias tabelas (não é o nosso caso)
    #group = ModelFormField(GroupForm)

    group_id = SelectField('Group Id', validators=[Optional()], coerce=int)