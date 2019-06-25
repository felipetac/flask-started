from . import Base
from app import DB, MA

ROLES = DB.Table('auth_group_role', Base.metadata,
    DB.Column('role_id', DB.Integer, DB.ForeignKey('auth_role.id'), primary_key=True),
    DB.Column('group_id', DB.Integer, DB.ForeignKey('auth_group.id'), primary_key=True)
)

class Role(Base):

    __tablename__ = 'auth_role'

    name = DB.Column(DB.String(128), nullable=False, unique=True)
    description = DB.Column(DB.String(500), nullable=True)

class RoleSchema(MA.ModelSchema):
    class Meta:
        model = Role
