from lib import GeoPoint


COEFF = 1000000


def nextpoint(latitude_a, longitude_a, distance, bearing):
    (latitude_a, longitude_a, distance, bearing) = (latitude_a / COEFF, longitude_a / COEFF, distance / COEFF * 1000, bearing / COEFF)
    p_a = GeoPoint(latitude_a, longitude_a)
    p_b = p_a.nextpoint(bearing, distance)
    return {'latitude_b': p_b.latitude,
            'longitude_b': p_b.longitude,
            'p_a_elevation': p_a.elevation,
            'p_b_elevation': p_b.elevation,
            }


def distance(la_a, lo_a, la_b, lo_b):
    (la_a, lo_a, la_b, lo_b) = (la_a / COEFF, lo_a / COEFF, la_b / COEFF, lo_b / COEFF)
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
            'p_a_elevation': p_a.elevation,
            'p_b_elevation': p_b.elevation,
            }
