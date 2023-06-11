from flask import Flask
from flask_cors import CORS


app = Flask(__name__)

try:
    app.config.from_object('app.productionconfig')
except ImportError:
    app.config.from_object('app.config')

CORS(app, resources={r"/mlc/api/*": {"origins": ["http://localhost:5173"]}})


from app.v01.views import v01  # noqa

app.register_blueprint(v01, url_prefix='/mlc/api/v0.1')
