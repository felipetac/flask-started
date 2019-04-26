from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.event import listen
from app import DB, MA
from app.mod_auth.model import Base


class User(Base):

    __tablename__ = 'auth_user'

    # User Name
    name = DB.Column(DB.String(200), nullable=False)

    # Identification Data: email & password
    email = DB.Column(DB.String(200), nullable=False, unique=True)
    password = DB.Column(DB.String(200), nullable=False)
    group_id = DB.Column(DB.Integer, DB.ForeignKey('auth_group.id'), nullable=True)

    @staticmethod
    def _hash_password(mapper, connection, target):
        user = target
        user.password = generate_password_hash(user.password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % (self.name)


class UserSchema(MA.ModelSchema):
    class Meta:
        model = User


listen(User, 'before_insert', User._hash_password)
listen(User, 'before_update', User._hash_password)
