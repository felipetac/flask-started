# from werkzeug.security import generate_password_hash, check_password_hash
# from sqlalchemy.event import listen
from app import DB, MA, PS
from . import Base
from .group import Group
from flask import current_app
# Hash password Automagic
from sqlalchemy_utils import PasswordType, force_auto_coercion, EmailType


class User(Base):

    __tablename__ = 'auth_user'

    # User Name
    name = DB.Column(DB.String(200), nullable=False)

    # Identification Data: email & password
    email = DB.Column(EmailType, nullable=False, unique=True)
    password = DB.Column(PasswordType(
        # The returned dictionary is forwarded to the CryptContext
        onload=lambda **kwargs: dict(schemes=PS, **kwargs)
    ), nullable=False)
    group_id = DB.Column(DB.Integer, DB.ForeignKey('auth_group.id'))
    group = DB.relationship(Group)


class UserSchema(MA.ModelSchema):
    class Meta:
        model = User
