import redis
import rq
from flask import Flask, redirect, url_for

# from werkzeug.routing import FloatConverter as BaseFloatConverter


# class FloatConverter(BaseFloatConverter):
#     regex = r'-?\d+(?:\.\d+)?'


app = Flask(__name__)
# app.url_map.converters['float'] = FloatConverter

try:
    app.config.from_object('app.productionconfig')
except ImportError:
    app.config.from_object('app.config')

app.redis = redis.from_url('redis://{0}:{1}/{2}'.format(app.config['REDIS_HOST'], app.config['REDIS_PORT'], app.config['REDIS_DB']))
app.task_queue = rq.Queue('default', connection=app.redis)


from app.v01.views import v01  # noqa

app.register_blueprint(v01, url_prefix='/mlc/')


@app.route('/')
def index():
    return redirect(url_for('v01.index'))
