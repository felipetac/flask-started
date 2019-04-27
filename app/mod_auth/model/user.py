#from werkzeug.security import generate_password_hash, check_password_hash
#from sqlalchemy.event import listen
from app import DB, MA
from . import Base
from .group import Group
from sqlalchemy_utils import PasswordType # Hash password Automagic


class User(Base):

    __tablename__ = 'auth_user'

    # User Name
    name = DB.Column(DB.String(200), nullable=False)

    # Identification Data: email & password
    email = DB.Column(DB.String(200), nullable=False, unique=True)
    password = DB.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
    ), nullable=False)
    group_id = DB.Column(DB.Integer, DB.ForeignKey('auth_group.id'))
    group = DB.relationship(Group)

    #def verify_password(self, password):
    #    """
    #    Check if hashed password matches actual password
    #    """
    #    return check_password_hash(self.password_hash, password)


class UserSchema(MA.ModelSchema):
    class Meta:
        model = User
