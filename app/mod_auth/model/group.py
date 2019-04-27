from app import DB, MA
from . import Base
from .role import ROLES


class Group(Base):

    __tablename__ = 'auth_group'

    name = DB.Column(DB.String(128), nullable=False, unique=True)
    initials = DB.Column(DB.String(10), nullable=False, unique=True)
    parent_id = DB.Column(DB.Integer, DB.ForeignKey('auth_group.id'),
                          nullable=True)
    children = DB.relationship('Group', lazy="joined", join_depth=2)
    roles = DB.relationship('Role', secondary=ROLES, lazy='subquery',
                            backref=DB.backref('groups', lazy=True))


class GroupSchema(MA.ModelSchema):
    class Meta:
        model = Group
