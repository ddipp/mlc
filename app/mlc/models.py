from datetime import datetime
from app import db

from app.auth.models import UserModel


class SiteModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(UserModel.id), nullable=False)  # Reference to user
    user = db.relationship(UserModel, backref='cost', cascade="all")  # back Reference to user
    name = db.Column(db.String(100))
    height = db.Column(db.Integer())
    latitude = db.Column(db.Numeric(10, 7))
    longitude = db.Column(db.Numeric(10, 7))
    dt = db.Column(db.DateTime, default=datetime.utcnow)
