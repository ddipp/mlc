from flask import Blueprint, render_template

from .forms import DistanceForm, NextPointForm

v01 = Blueprint('v01', __name__)


@v01.route('/')
def index():
    return render_template('index.html', title="Home")


@v01.route('points')
def points():
    distance_form = DistanceForm()
    nextpoint_form = NextPointForm()
    return render_template('points.html', title="Points",
                           distance_form=distance_form, nextpoint_form=nextpoint_form)
