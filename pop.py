#!/usr/bin/env python
from app import app, db
from app.auth.models import UserModel, RoleModel

from app.mlc.models import SiteModel


def test_connection():
    with app.app_context():

        # Роли
        role1 = RoleModel(name='mails', description='For mails')
        db.session.add(role1)
        db.session.commit()
        role2 = RoleModel(name='admin', description='For superuser')
        db.session.add(role2)
        db.session.commit()

        # Пользователи
        user1 = UserModel(email='test@test.com', password='test')
        user1.roles.append(role1)
        user1.roles.append(role2)
        db.session.add(user1)
        db.session.commit()

        user2 = UserModel(email='test1@test.com', password='test1')
        user2.roles.append(role1)
        db.session.add(user2)
        db.session.commit()

        site1 = SiteModel(user=user2, name="site1user2", height=11, latitude=56.1234561, longitude=66.1234561)
        site2 = SiteModel(user=user2, name="site2user2", height=12, latitude=56.1234562, longitude=66.1234562)
        site3 = SiteModel(user=user1, name="site1user1", height=13, latitude=56.1234563, longitude=66.1234563)
        site4 = SiteModel(user=user1, name="site2user1", height=14, latitude=56.1234564, longitude=66.1234564)
        db.session.add_all([site1, site2, site3, site4])
        db.session.commit()


test_connection()
