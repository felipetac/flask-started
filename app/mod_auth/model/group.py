from app import DB, MA
from . import Base
from .role import ROLES
from marshmallow import fields
from app.mod_auth.model.role import RoleSchema


class Group(Base):

    __tablename__ = 'auth_group'

    name = DB.Column(DB.String(128), nullable=False, unique=True)
    initials = DB.Column(DB.String(10), nullable=False, unique=True)
    parent_id = DB.Column(DB.Integer, DB.ForeignKey('auth_group.id'),
                          nullable=True)
    children = DB.relationship('Group', lazy="joined", join_depth=2)
    roles = DB.relationship('Role', secondary=ROLES,
                            backref=DB.backref('groups'))


class GroupSchema(MA.ModelSchema):
    class Meta:
        model = Group

    children = fields.Nested("GroupSchema", many=True)
    roles = fields.Nested(RoleSchema, many=True, 
                          exclude=("date_created",
                                   "date_modified", ))
