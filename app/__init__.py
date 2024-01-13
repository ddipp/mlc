import redis
import rq

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask import Flask, render_template

# from werkzeug.routing import FloatConverter as BaseFloatConverter


# class FloatConverter(BaseFloatConverter):
#     regex = r'-?\d+(?:\.\d+)?'


app = Flask(__name__, static_folder='static', template_folder='templates')
# app.url_map.converters['float'] = FloatConverter

try:
    app.config.from_object('app.productionconfig')
except ImportError:
    app.config.from_object('app.config')

db = SQLAlchemy(app)

if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
    from sqlalchemy.engine import Engine
    from sqlalchemy import event

    @event.listens_for(Engine, 'connect')
    def set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute('PRAGMA foreign_keys=ON')
        cursor.close()

migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

app.redis = redis.from_url('redis://{0}:{1}/{2}'.format(app.config['REDIS_HOST'], app.config['REDIS_PORT'], app.config['REDIS_DB']))
app.task_queue = rq.Queue('default', connection=app.redis)


from app.mlc.views import mlc  # noqa
from app.auth.views import auth  # noqa

app.register_blueprint(mlc, url_prefix='/mlc/')
app.register_blueprint(auth, url_prefix='/auth/')


@app.route('/')
def index():
    return render_template('index.html', title="Home")
