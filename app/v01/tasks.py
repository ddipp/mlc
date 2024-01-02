from lib import GeoPoint, RadioProfile


def profile(tx_power: int, frequency: int, receiver_sensitivity: float,
            antenna_gain_a: float, latitude_a: float, longitude_a: float, height_a: int,
            antenna_gain_b: float, latitude_b: float, longitude_b: float, height_b: int):
    p_a = GeoPoint(latitude_a, longitude_a)
    p_a.h = height_a
    p_b = GeoPoint(latitude_b, longitude_b)
    p_b.h = height_b
    radio_profile = RadioProfile(p_a, p_a.h, p_b, p_b.h, frequency)
    radio_profile.set_radio_parameters(tx_power=tx_power, receiver_sensitivity=receiver_sensitivity,
                                       antenna_gain_a=antenna_gain_a, antenna_gain_b=antenna_gain_b)
    return {'distance': radio_profile.length / 1000,
            'az_a_b': p_a.azimuth(p_b),
            'az_b_a': p_b.azimuth(p_a),
            'a_elevation': p_a.elevation,
            'b_elevation': p_b.elevation,
            'a_height': p_a.h,
            'b_height': p_b.h,
            'line_of_sight': radio_profile.line_of_sight,
            'visibility_in_0_6_fresnel_zone': radio_profile.visibility_in_0_6_fresnel_zone
            }


def distance(latitude_a: float, longitude_a: float, latitude_b: float, longitude_b: float):
    """
    Calculation distance (along the line of sight and along the surface of the sphere), azimuths, and heights of geographical points.
    """
    p_a = GeoPoint(latitude_a, longitude_a)
    p_b = GeoPoint(latitude_b, longitude_b)
    distance = p_a.distance_to(p_b) / 1000
    arc_distance = p_a.arc_distance_to(p_b) / 1000
    az_a_b = p_a.azimuth(p_b)
    az_b_a = p_b.azimuth(p_a)
    return {'distance': distance,
            'arc_distance': arc_distance,
            'az_a_b': az_a_b,
            'az_b_a': az_b_a,
            'a_elevation': p_a.elevation,
            'b_elevation': p_b.elevation,
            }


def nextpoint(latitude_a: float, longitude_a: float, distance: float, bearing: float):
    """
    Calculation of the height and coordinates of a geographic point based on a given first point, azimuth and distance.
    """
    p_a = GeoPoint(latitude_a, longitude_a)
    p_b = p_a.nextpoint(bearing, distance)
    return {'b_latitude': p_b.latitude,
            'b_longitude': p_b.longitude,
            'a_elevation': p_a.elevation,
            'b_elevation': p_b.elevation,
            }
