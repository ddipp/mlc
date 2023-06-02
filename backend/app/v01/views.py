from flask import Blueprint, jsonify
from lib import GeoPoint

v01 = Blueprint('v01', __name__)

COEFF = 1000000


@v01.route('distance/<int(signed=True):la_a>/<int(signed=True):lo_a>/<int(signed=True):la_b>/<int(signed=True):lo_b>')
def distance(la_a, lo_a, la_b, lo_b):
    (la_a, lo_a, la_b, lo_b) = (la_a / COEFF, lo_a / COEFF, la_b / COEFF, lo_b / COEFF)
    p_a = GeoPoint(la_a, lo_a)
    p_b = GeoPoint(la_b, lo_b)
    distance = p_a.distance_to(p_b) / 1000
    arc_distance = p_a.arc_distance_to(p_b) / 1000
    az_a_b = p_a.azimuth(p_b)
    az_b_a = p_b.azimuth(p_a)
    return jsonify(distance="{:.3f}".format(distance),
                   arc_distance="{:.3f}".format(arc_distance),
                   az_a_b="{:.1f}".format(az_a_b),
                   az_b_a="{:.1f}".format(az_b_a),
                   p_a_elevation=p_a.elevation,
                   p_b_elevation=p_b.elevation,
                   )
