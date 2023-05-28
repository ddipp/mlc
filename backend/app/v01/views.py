from flask import Blueprint, jsonify


v01 = Blueprint('v01', __name__)


@v01.route('/test')
def root():
    return jsonify(name="testname testfamily")
