from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, HiddenField, StringField, validators
from flask_login import current_user
from wtforms_sqlalchemy.fields import QuerySelectField

from .models import SiteModel


def sites_res():
    return SiteModel.query.filter(SiteModel.user == current_user).order_by(SiteModel.dt.desc()).all()


class LinkForm(FlaskForm):
    tx_power = IntegerField("Tx power (dBm)", [validators.InputRequired(), validators.NumberRange(min=-10, max=50)])
    frequency = IntegerField("Frequency (GHz)", [validators.InputRequired(), validators.NumberRange(min=3, max=90)])
    antenna_a_gain = DecimalField("Antenna gain (dB)", [validators.InputRequired(), validators.NumberRange(min=0, max=90)], places=1)
    antenna_a_height = IntegerField("Height (m)", [validators.InputRequired(), validators.NumberRange(min=0, max=300)])
    antenna_b_gain = DecimalField("Antenna gain (dB)", [validators.InputRequired(), validators.NumberRange(min=0, max=90)], places=1)
    antenna_b_height = IntegerField("Height (m)", [validators.InputRequired(), validators.NumberRange(min=0, max=300)])
    site_a = QuerySelectField(query_factory=sites_res, get_label='name')
    site_b = QuerySelectField(query_factory=sites_res, get_label='name')


class SiteForm(FlaskForm):
    latitude = DecimalField("Latitude", [validators.InputRequired(), validators.NumberRange(min=-90, max=90)], places=7)
    longitude = DecimalField("Longitude", [validators.InputRequired(), validators.NumberRange(min=-180, max=180)], places=7)
    name = StringField("Site name", [validators.InputRequired()])


class ProfileForm(FlaskForm):
    url = HiddenField()
    tx_power = IntegerField("Tx power (dBm)", [validators.InputRequired(), validators.NumberRange(min=-10, max=50)])
    frequency = IntegerField("Frequency (GHz)", [validators.InputRequired(), validators.NumberRange(min=3, max=90)])
    receiver_sensitivity = DecimalField("Receiver sensitivity (dBm)", [validators.InputRequired(), validators.NumberRange(min=-100, max=0)])
    antenna_a_gain = DecimalField("Antenna gain (dB)", [validators.InputRequired(), validators.NumberRange(min=0, max=90)], places=1)
    latitude_a = DecimalField("Latitude", [validators.InputRequired(), validators.NumberRange(min=-90, max=90)], places=7)
    longitude_a = DecimalField("Longitude", [validators.InputRequired(), validators.NumberRange(min=-180, max=180)], places=7)
    antenna_a_height = IntegerField("Height (m)", [validators.InputRequired(), validators.NumberRange(min=0, max=300)])
    antenna_b_gain = DecimalField("Antenna gain (dB)", [validators.InputRequired(), validators.NumberRange(min=0, max=90)], places=1)
    latitude_b = DecimalField("Latitude", [validators.InputRequired(), validators.NumberRange(min=-90, max=90)], places=7)
    longitude_b = DecimalField("Longitude", [validators.InputRequired(), validators.NumberRange(min=-180, max=180)], places=7)
    antenna_b_height = IntegerField("Height (m)", [validators.InputRequired(), validators.NumberRange(min=0, max=300)])


class DistanceForm(FlaskForm):
    url = HiddenField()
    latitude_a = DecimalField("Latitude", [validators.InputRequired(), validators.NumberRange(min=-90, max=90)], places=7)
    longitude_a = DecimalField("Longitude", [validators.InputRequired(), validators.NumberRange(min=-180, max=180)], places=7)
    latitude_b = DecimalField("Latitude", [validators.InputRequired(), validators.NumberRange(min=-90, max=90)], places=7)
    longitude_b = DecimalField("Longitude", [validators.InputRequired(), validators.NumberRange(min=-180, max=180)], places=7)


class NextPointForm(FlaskForm):
    url = HiddenField()
    latitude = DecimalField("Latitude", [validators.InputRequired(), validators.NumberRange(min=-90, max=90)], places=7)
    longitude = DecimalField("Longitude", [validators.InputRequired(), validators.NumberRange(min=-180, max=180)], places=7)
    distance = DecimalField("Distance (km)", [validators.DataRequired(), validators.NumberRange(min=0, max=40000)])
    bearing = DecimalField("Bearing (°)", [validators.InputRequired(), validators.NumberRange(min=-360, max=360)], places=2)
