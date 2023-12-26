from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, HiddenField, validators


class ProfileForm(FlaskForm):
    url = HiddenField()
    tx_power = IntegerField("Tx power (dBm)", [validators.InputRequired(), validators.NumberRange(min=-10, max=50)])
    frequency = IntegerField("Frequency (GHz)", [validators.InputRequired(), validators.NumberRange(min=3, max=90)])
    receiver_sensitivity = IntegerField("Receiver sensitivity (dBm)", [validators.InputRequired(), validators.NumberRange(min=-100, max=0)])
    antenna_gain_a = DecimalField("Antenna gain (dB)", [validators.InputRequired(), validators.NumberRange(min=0, max=90)])
    latitude_a = DecimalField("Latitude", [validators.InputRequired(), validators.NumberRange(min=-90, max=90)])
    longitude_a = DecimalField("Longitude", [validators.InputRequired(), validators.NumberRange(min=-180, max=180)])
    height_a = IntegerField("Height (m)", [validators.InputRequired(), validators.NumberRange(min=0, max=300)])
    antenna_gain_b = DecimalField("Antenna gain (dB)", [validators.InputRequired(), validators.NumberRange(min=0, max=90)])
    latitude_b = DecimalField("Latitude", [validators.InputRequired(), validators.NumberRange(min=-90, max=90)])
    longitude_b = DecimalField("Longitude", [validators.InputRequired(), validators.NumberRange(min=-180, max=180)])
    height_b = IntegerField("Height (m)", [validators.InputRequired(), validators.NumberRange(min=0, max=300)])


class DistanceForm(FlaskForm):
    url = HiddenField()
    latitude_a = DecimalField("Latitude", [validators.InputRequired(), validators.NumberRange(min=-90, max=90)])
    longitude_a = DecimalField("Longitude", [validators.InputRequired(), validators.NumberRange(min=-180, max=180)])
    latitude_b = DecimalField("Latitude", [validators.InputRequired(), validators.NumberRange(min=-90, max=90)])
    longitude_b = DecimalField("Longitude", [validators.InputRequired(), validators.NumberRange(min=-180, max=180)])


class NextPointForm(FlaskForm):
    url = HiddenField()
    latitude = DecimalField("Latitude", [validators.InputRequired(), validators.NumberRange(min=-90, max=90)])
    longitude = DecimalField("Longitude", [validators.InputRequired(), validators.NumberRange(min=-180, max=180)])
    distance = DecimalField("Distance (km)", [validators.DataRequired(), validators.NumberRange(min=0, max=40000)])
    bearing = DecimalField("Bearing (°)", [validators.InputRequired(), validators.NumberRange(min=-360, max=360)])
