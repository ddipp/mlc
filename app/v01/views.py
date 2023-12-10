from flask import Blueprint, render_template

from .forms import DistanceForm, NextPointForm

v01 = Blueprint('v01', __name__)


@v01.route('/')
def index():
    return render_template('index.html', title="Home")


@v01.route('distance')
def distance():
    distance_form = DistanceForm()
    return render_template('distance.html', title="Distance",
                           distance_form=distance_form)


@v01.route('nextpoint')
def nextpoint():
    nextpoint_form = NextPointForm()
    return render_template('nextpoint.html', title="NextPoint",
                           nextpoint_form=nextpoint_form)
