from lib import GeoPoint


def distance(la_a: float, lo_a: float, la_b: float, lo_b: float):
    """
    Calculation distance (along the line of sight and along the surface of the sphere), azimuths, and heights of geographical points.
    """
    p_a = GeoPoint(la_a, lo_a)
    p_b = GeoPoint(la_b, lo_b)
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


def nextpoint(la_a: float, lo_a: float, distance: float, bearing: float):
    """
    Calculation of the height and coordinates of a geographic point based on a given first point, azimuth and distance.
    """
    p_a = GeoPoint(la_a, lo_a)
    p_b = p_a.nextpoint(bearing, distance)
    return {'b_latitude': p_b.latitude,
            'b_longitude': p_b.longitude,
            'a_elevation': p_a.elevation,
            'b_elevation': p_b.elevation,
            }
