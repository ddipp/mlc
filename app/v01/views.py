from flask import Blueprint, render_template

v01 = Blueprint('v01', __name__)


@v01.route('/')
def index():
    return render_template('index.html')
