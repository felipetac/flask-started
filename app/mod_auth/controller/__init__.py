# Define the blueprint: 'auth', set its url prefix: app.url/auth
from flask import Blueprint

MOD_AUTH = Blueprint('auth', __name__, url_prefix='/auth')

from app.mod_auth.controller.auth import * # pylint: disable=wrong-import-position
from app.mod_auth.controller.user import * # pylint: disable=wrong-import-position
from app.mod_auth.controller.group import * # pylint: disable=wrong-import-position
from app.mod_auth.controller.role import * # pylint: disable=wrong-import-position
