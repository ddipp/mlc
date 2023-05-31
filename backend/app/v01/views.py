from flask import Blueprint, jsonify


v01 = Blueprint('v01', __name__)


@v01.route('/test')
def root():
    return jsonify(name="testname testfamily")


@v01.route('distance/<int(signed=True):la_a>/<int(signed=True):lo_a>/<int(signed=True):la_b>/<int(signed=True):lo_b>')
def distance(la_a, lo_a, la_b, lo_b):
    return jsonify(distance="{:.2f}".format(la_a + 20))
