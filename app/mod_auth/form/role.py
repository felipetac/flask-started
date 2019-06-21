from . import RestForm
from app.mod_auth.model.role import Role


class RoleForm(RestForm):

    class Meta:
        model = Role

    def sanitize(self):
        self.name.data = (self.name.data).strip().replace(" ", "-").upper()