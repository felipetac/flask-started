# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, PasswordField  # BooleanField

# Import Form validators
from wtforms.validators import Required, Email

from app.mod_auth.form import RestForm


class GroupForm(RestForm):

    name = TextField('Nome do Grupo',
                     [Required(message='Precisa fornecer o nome do grupo.')])
    initials = TextField('Sigla do Grupo',
                         [Required(message='Precisa fornecer a sigla.')])
    parent = TextField('Grupo Pai',
                       [Required(message='Precisa fornecer o id do grupo pai.')])
    roles = TextField('Regras',
                      [Required(message='Precisa fornecer o array de regras.')])
    users = TextField('Usuarios',
                      [Required(message='Precisa fornecer o array de usuarios.')])
