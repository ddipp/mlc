from flask import Blueprint, render_template

from .forms import DistanceForm, NextPointForm

from lib import GeoPoint


v01 = Blueprint('v01', __name__)


@v01.route('/', methods=['GET'])
def index():
    return render_template('index.html', title="Home")


@v01.route('distance', methods=['GET', 'POST'])
def distance():
    answer = {}
    distance_form = DistanceForm()
    if distance_form.validate_on_submit():
        p_a = GeoPoint(distance_form.latitude_a.data, distance_form.longitude_a.data)
        p_b = GeoPoint(distance_form.latitude_b.data, distance_form.longitude_b.data)
        answer['distance'] = p_a.distance_to(p_b) / 1000
        answer['arc_distance'] = p_a.arc_distance_to(p_b) / 1000
        answer['az_a_b'] = p_a.azimuth(p_b)
        answer['az_b_a'] = p_b.azimuth(p_a)
        answer['a_elevation'] = p_a.elevation
        answer['b_elevation'] = p_b.elevation
    else:
        pass
    return render_template('distance.html', title="Distance",
                           distance_form=distance_form, answer=answer)


@v01.route('nextpoint', methods=['GET', 'POST'])
def nextpoint():
    nextpoint_form = NextPointForm()
    return render_template('nextpoint.html', title="Next point",
                           nextpoint_form=nextpoint_form)
