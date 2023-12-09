from flask_wtf import FlaskForm
from wtforms import DecimalField, validators


class DistanceForm(FlaskForm):
    latitude_a = DecimalField("Latitude", [validators.DataRequired()])
    longitude_a = DecimalField("Longitude", [validators.DataRequired()])
    latitude_b = DecimalField("Latitude", [validators.DataRequired()])
    longitude_b = DecimalField("Longitude", [validators.DataRequired()])


class NextPointForm(FlaskForm):
    latitude = DecimalField("Latitude", [validators.DataRequired()])
    longitude = DecimalField("Longitude", [validators.DataRequired()])
    distance = DecimalField("Distance", [validators.DataRequired()])
    bearing = DecimalField("Bearing (°)", [validators.DataRequired()])
