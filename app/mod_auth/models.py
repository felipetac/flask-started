from app.container import DB, MA
from app.mod_user.models import User

# Define a base model for other database tables to inherit

class Base(DB.Model):

    __abstract__ = True

    id = DB.Column(DB.Integer, primary_key=True)
    date_created = DB.Column(DB.DateTime, default=DB.func.current_timestamp())
    date_modified = DB.Column(DB.DateTime, default=DB.func.current_timestamp(),
                              onupdate=DB.func.current_timestamp())

ROLES = DB.Table('auth_group_role',
                 DB.Column('role_id', DB.Integer, DB.ForeignKey(
                     'auth_role.id'), primary_key=True),
                 DB.Column('group_id', DB.Integer, DB.ForeignKey(
                     'auth_group.id'), primary_key=True)
                 )

class Role(Base):

    __tablename__ = 'auth_role'

    name = DB.Column(DB.String(128), nullable=False, unique=True)
    decription = DB.Column(DB.String(500), nullable=True)

class RoleSchema(MA.ModelSchema):
    class Meta:
        model = Role

class Group(Base):

    __tablename__ = 'auth_group'

    name = DB.Column(DB.String(128), nullable=False, unique=True)
    initials = DB.Column(DB.String(10), nullable=False, unique=True)
    parent = DB.Column(DB.Integer, DB.ForeignKey('auth_group.id'),
                       nullable=True)
    roles = DB.relationship('Role', secondary=ROLES, lazy='subquery',
                            backref=DB.backref('groups', lazy=True))
    users = DB.relationship(User, backref='group', lazy=True)

    def hydrate(self, form):
        """
        Hydrate form data into user model
        """
        self.name = form.name.data
        self.initials = form.email.data
        self.parent = form.parent.data
        self.roles = form.roles.data
        self.users = form.users.data

class GroupSchema(MA.ModelSchema):
    class Meta:
        model = Group
