from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class RoleModel(db.Model):
    __tablename__ = 'auth_roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return str(self.name)


class UserModel(db.Model, UserMixin):
    __tablename__ = 'auth_users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, default=datetime.utcnow)
    roles = db.relationship('RoleModel', secondary="auth_users_roles", backref=db.backref('users'))
    password_hash = db.Column(db.String(256))

    def is_admin(self):
        adminrole = RoleModel.query.filter_by(name='admin').first()
        return adminrole in self.roles

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def password(self):
        raise AttributeError('password not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        # or whatever other hashing function you like.

    def __repr__(self):
        return str(self.email)


class Auth_Roles_Users(db.Model):
    __tablename__ = 'auth_users_roles'
    __table_args__ = (db.UniqueConstraint('user_id', 'role_id'),)
    user_id = db.Column(db.Integer, db.ForeignKey(UserModel.id, ondelete="CASCADE"), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey(RoleModel.id, ondelete="CASCADE"), primary_key=True)
