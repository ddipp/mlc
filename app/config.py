import os
from pathlib import Path

basedir = os.path.abspath(os.path.dirname(__file__))

CACHE_DIR_PROFILE = Path.cwd() / 'data' / 'cache'

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 3

CSRF_ENABLED = True
SECRET_KEY = 'a random string'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_ECHO = True
# SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
