from datetime import datetime
from app import db

from app.auth.models import UserModel


class SiteModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(UserModel.id), nullable=False)  # Reference to user
    user = db.relationship(UserModel, backref='site', cascade="all")  # back Reference to user
    name = db.Column(db.String(100))
    elevation = db.Column(db.Integer())
    latitude = db.Column(db.Numeric(9, 6))
    longitude = db.Column(db.Numeric(9, 6))
    dt = db.Column(db.DateTime, default=datetime.utcnow)


class LinkModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(UserModel.id), nullable=False)  # Reference to user
    user = db.relationship(UserModel, backref='link', cascade="all")  # back Reference to user
    site_a_id = db.Column(db.Integer, db.ForeignKey(SiteModel.id, ondelete='CASCADE'))
    site_b_id = db.Column(db.Integer, db.ForeignKey(SiteModel.id, ondelete='CASCADE'))
    site_a = db.relationship(SiteModel, foreign_keys=[site_a_id], backref='link_a')  # back Reference to site
    site_b = db.relationship(SiteModel, foreign_keys=[site_b_id], backref='link_b')  # back Reference to site

    antenna_a_height = db.Column(db.Integer())
    antenna_b_height = db.Column(db.Integer())
    frequency = db.Column(db.Integer())
    tx_power = db.Column(db.Integer())
    antenna_a_gain = db.Column(db.Numeric(3, 1))
    antenna_b_gain = db.Column(db.Numeric(3, 1))

    dt = db.Column(db.DateTime, default=datetime.utcnow)
