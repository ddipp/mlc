from flask_wtf import FlaskForm
from wtforms import DecimalField, HiddenField, validators


class DistanceForm(FlaskForm):
    url = HiddenField()
    latitude_a = DecimalField("Latitude", [validators.InputRequired(), validators.NumberRange(min=-90, max=90)])
    longitude_a = DecimalField("Longitude", [validators.InputRequired(), validators.NumberRange(min=-180, max=180)])
    latitude_b = DecimalField("Latitude", [validators.InputRequired(), validators.NumberRange(min=-90, max=90)])
    longitude_b = DecimalField("Longitude", [validators.InputRequired(), validators.NumberRange(min=-180, max=180)])


class NextPointForm(FlaskForm):
    latitude = DecimalField("Latitude", [validators.InputRequired(), validators.NumberRange(min=-90, max=90)])
    longitude = DecimalField("Longitude", [validators.InputRequired(), validators.NumberRange(min=-180, max=180)])
    distance = DecimalField("Distance (km)", [validators.DataRequired(), validators.NumberRange(min=0, max=40000)])
    bearing = DecimalField("Bearing (°)", [validators.InputRequired(), validators.NumberRange(min=-360, max=360)])
