import json
import math as m
from lib.srtm import srtm

EARTH_RADIUS = 6371009


class GeoPoint:
    """GeoPoint
       Geographical point.
       Two coordinates (latitude and longitude), optionally height above sea level.
       If the height is not specified, then the height is taken from the SRTM3 data.
    """

    def __init__(self, latitude: float, longitude: float, elevation: int = None, name: str = ''):
        """ Two coordinates (latitude and longitude), optionally height above sea level.
            If the height is not specified, then the height is taken from the SRTM3 data.
        """
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        if elevation is None:
            self.elevation = srtm.get_elevation_point(latitude, longitude)
        else:
            self.elevation = elevation

    def azimuth(self, point) -> float:
        """ Azimuth between two points in degrees """
        d_longitude = point.rlongitude - self.rlongitude
        az_radians = m.atan2(m.sin(d_longitude) * m.cos(point.rlatitude),
                             m.cos(self.rlatitude) * m.sin(point.rlatitude)
                             - m.sin(self.rlatitude) * m.cos(point.rlatitude) * m.cos(d_longitude)
                             )
        return m.degrees(az_radians) if m.degrees(az_radians) >= 0 else m.degrees(az_radians) + 360

    def nextpoint(self, azimuth: float, distance: float):
        """ Calculates the coordinates of the next point in the given azimuth and distance.
            The azimuth is given in degrees.
            Distance in meters.
        """
        dr = distance / EARTH_RADIUS
        drs = m.sin(dr)
        drc = m.cos(dr)
        start_lat_cos = m.cos(self.rlatitude)
        start_lat_sin = m.sin(self.rlatitude)

        end_lat_rads = m.asin((start_lat_sin * drc) + (start_lat_cos * drs * m.cos(m.radians(azimuth))))

        end_lon_rads = self.rlongitude + m.atan2(m.sin(m.radians(azimuth)) * drs * start_lat_cos,
                                                 drc - start_lat_sin * m.sin(end_lat_rads))

        return GeoPoint(latitude=m.degrees(end_lat_rads), longitude=m.degrees(end_lon_rads))

    def distance_to(self, point) -> float:
        """ Calculation of the distance between two points in meters in a straight line.
            For example, the distance between two points:
            - Mount Elbrus
            - and a point with the same coordinates, but with a height above sea level of 0 meters
            = 5519 meters
        """
        return m.sqrt((self.x - point.x)**2 + (self.y - point.y)**2 + (self.z - point.z)**2)

    def arc_distance_to(self, point) -> float:
        """ Calculation of the distance between two points in meters on the surface of the planet.
            For example, the distance between two points:
            - Mount Elbrus
            - and a point with the same coordinates, but with a height above sea level of 0 meters
            = 0 meters
        """
        dx = m.cos(point.rlatitude) * m.cos(point.rlongitude) - m.cos(self.rlatitude) * m.cos(self.rlongitude)
        dy = m.cos(point.rlatitude) * m.sin(point.rlongitude) - m.cos(self.rlatitude) * m.sin(self.rlongitude)
        dz = m.sin(point.rlatitude) - m.sin(self.rlatitude)
        c = m.sqrt(dx**2 + dy**2 + dz**2)
        d_c = 2 * m.asin(c / 2)
        return EARTH_RADIUS * d_c

    # The formula for back conversion:

    #    lat = asin(z / R)
    #    lon = atan2(y, x)
    # Don’t forget to convert back from radians to degrees.

    # Coordinates in 3D projection centered on the center of the planet
    @property
    def x(self) -> float:
        if self.elevation:
            return (EARTH_RADIUS + self.elevation) * m.cos(self.rlatitude) * m.cos(self.rlongitude)
        else:
            return EARTH_RADIUS * m.cos(self.rlatitude) * m.cos(self.rlongitude)

    @property
    def y(self) -> float:
        if self.elevation:
            return (EARTH_RADIUS + self.elevation) * m.cos(self.rlatitude) * m.sin(self.rlongitude)
        else:
            return EARTH_RADIUS * m.cos(self.rlatitude) * m.sin(self.rlongitude)

    @property
    def z(self) -> float:
        if self.elevation:
            return (EARTH_RADIUS + self.elevation) * m.sin(self.rlatitude)
        else:
            return EARTH_RADIUS * m.sin(self.rlatitude)

    # Coordinate in radians
    @property
    def rlatitude(self) -> float:
        return m.radians(self.latitude)

    # Coordinate in radians
    @property
    def rlongitude(self) -> float:
        return m.radians(self.longitude)

    def to_json(self):
        """ Serialization of class data. """
        return json.dumps(vars(self))

    def __str__(self):
        return f'GeoPoint name {self.name}\t{self.latitude}, {self.longitude}, {self.elevation}'
