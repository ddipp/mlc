from flask import Blueprint, jsonify


v01 = Blueprint('v01', __name__)


@v01.route('/test')
def root():
    return jsonify(name="testname testfamily")


@v01.route('distance/<int(signed=True):lat_1>')
def distance(lat_1):
    return jsonify(distance="{:.2f}".format(lat_1))
