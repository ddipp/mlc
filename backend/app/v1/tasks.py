import matplotlib.pyplot as plt

from lib import GeoPoint, GeoProfile


COEFF = 1000000


def profile(la_a, lo_a, la_b, lo_b, cache_dir):
    filename = "{0}_{1}_{2}_{3}.png".format(la_a, lo_a, la_b, lo_b)
    (la_a, lo_a, la_b, lo_b) = (la_a / COEFF, lo_a / COEFF, la_b / COEFF, lo_b / COEFF)
    p_a = GeoPoint(la_a, lo_a)
    p_b = GeoPoint(la_b, lo_b)

    distance = p_a.distance_to(p_b) / 1000
    az_a_b = p_a.azimuth(p_b)
    az_b_a = p_b.azimuth(p_a)

    profile = GeoProfile(p_a, p_b)
    profile_chart = profile.get_chart_data()
    plt.rcParams["figure.figsize"] = (14, 9)
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.grid(True)
    ax.plot(profile_chart['distance'], profile_chart['relief'], label="Elevation", linestyle='solid', linewidth=0.5)
    ax.fill_between(profile_chart['distance'], profile_chart['relief'], min(profile_chart['relief']), color='darkgreen', alpha=.4)

    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Elevation (m)')

    plt.legend()
    plt.title(
        f'Profile from "{profile.startpoint.name}" {profile.startpoint.latitude} {profile.startpoint.longitude} '
        f'to "{profile.stoppoint.name}" {profile.stoppoint.latitude} {profile.stoppoint.longitude}\n'
        f'Distance {profile.length / 1000:.2f} km')
    plt.savefig(cache_dir / filename, dpi=300, format='png')
    plt.close()
    return {'distance': distance,
            'az_a_b': az_a_b,
            'az_b_a': az_b_a,
            'p_a_elevation': p_a.elevation,
            'p_b_elevation': p_b.elevation,
            'filename': filename,
            }


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
