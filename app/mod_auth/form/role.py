from . import RestForm
from app.mod_auth.model.role import Role
from app.mod_auth.sanitizer import role_name


class RoleForm(RestForm):

    class Meta:
        model = Role
        field_args = {'name': {'filters': [lambda x: x, role_name]}}