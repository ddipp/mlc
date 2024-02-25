import matplotlib.pyplot as plt

from app import app, db
from app.mlc.models import SiteModel
from lib import GeoPoint, RadioProfile


def radio_profile_check(tx_power: int, frequency: int, receiver_sensitivity: float,
                        antenna_a_gain: float, latitude_a: float, longitude_a: float, antenna_a_height: int,
                        antenna_b_gain: float, latitude_b: float, longitude_b: float, antenna_b_height: int) -> dict:
    p_a = GeoPoint(latitude_a, longitude_a)
    p_b = GeoPoint(latitude_b, longitude_b)
    radio_profile = RadioProfile(p_a, antenna_a_height, p_b, antenna_b_height, frequency)
    radio_profile.set_radio_parameters(tx_power=tx_power, receiver_sensitivity=receiver_sensitivity,
                                       antenna_a_gain=antenna_a_gain, antenna_b_gain=antenna_b_gain)
    return {'visibility_in_0_6_fresnel_zone': radio_profile.visibility_in_0_6_fresnel_zone,
            'line_of_sight': radio_profile.line_of_sight
            }


def radio_profile_graph(tx_power: int, frequency: int, receiver_sensitivity: float,
                        antenna_a_gain: float, latitude_a: float, longitude_a: float, antenna_a_height: int,
                        antenna_b_gain: float, latitude_b: float, longitude_b: float, antenna_b_height: int, cache_dir: str,
                        name_a="", name_b="") -> dict:
    filename = "{0}_{1}_{2}_{3}_{4}_{5}_{6}_{7}_{8}.png".format(latitude_a, longitude_a, antenna_a_height, antenna_a_gain,
                                                                latitude_b, longitude_b, antenna_b_height, antenna_b_gain, frequency)
    p_a = GeoPoint(latitude_a, longitude_a, name=name_a)
    p_b = GeoPoint(latitude_b, longitude_b, name=name_b)

    radio_profile = RadioProfile(p_a, antenna_a_height, p_b, antenna_b_height, frequency)
    radio_profile.set_radio_parameters(tx_power=tx_power, receiver_sensitivity=receiver_sensitivity,
                                       antenna_a_gain=antenna_a_gain, antenna_b_gain=antenna_b_gain)
    profile_chart = radio_profile.get_chart_data
    plt.rcParams["figure.figsize"] = (14, 9)
    fig = plt.figure()
    ax = fig.add_subplot()

    ax.grid(True)
    ax.annotate(f'Antenna gain {radio_profile.antenna_a_gain:.1f} dBm\nHeight {antenna_a_height} m',
                xy=(0, profile_chart['los_height'][0]), xycoords='data',
                xytext=(0.1, 0.5), textcoords='axes fraction',
                horizontalalignment='left',
                arrowprops=dict(arrowstyle="simple",
                                fc="0.6", ec="none",
                                connectionstyle="arc3,rad=0.3"),
                bbox=dict(boxstyle="round", fc="1", alpha=0.5))

    ax.annotate(f'Antenna gain {radio_profile.antenna_b_gain:.1f} dBm\nHeight {antenna_b_height} m',
                xy=(profile_chart['distance'][-1], profile_chart['los_height'][-1]), xycoords='data',
                xytext=(0.9, 0.5), textcoords='axes fraction',
                horizontalalignment='right',
                arrowprops=dict(arrowstyle="simple",
                                fc="0.6", ec="none",
                                connectionstyle="arc3,rad=0.3"),
                bbox=dict(boxstyle="round", fc="1", alpha=0.5))

    ax.annotate(f'TX power {radio_profile.tx_power} dBm\nExpected RX Level {radio_profile.expected_signal_strength} dBm',
                xy=(0.5, 0.5), xycoords='axes fraction',
                horizontalalignment='center',
                bbox=dict(boxstyle="round", fc="1", alpha=0.5))

    ax.plot(profile_chart['distance'], profile_chart['relief'], label="Elevation", linestyle='solid', linewidth=0.5)
    ax.plot(profile_chart['distance'], profile_chart['relief_arc'],
            label="Surface with curvature of the earth", color='darkgreen', linewidth=0.5)

    ax.plot(profile_chart['distance'], profile_chart['los_height'], color='darkred', label="Line of sight", linewidth=0.5)

    ax.plot(profile_chart['distance'], profile_chart['frenzel_zone_1_60_top'],
            label="60% 1 Frenzel zone", color='red', linewidth=0.8, alpha=.8)
    ax.plot(profile_chart['distance'], profile_chart['frenzel_zone_1_60_bottom'], color='red', linewidth=0.8, alpha=.8)

    # ax.plot(profile_chart['distance'], profile_chart['frenzel_zone_1_top'], label="1 Frenzel zone", color='lightcoral', linewidth=0.5)
    # ax.plot(profile_chart['distance'], profile_chart['frenzel_zone_1_bottom'], color='lightcoral', linewidth=0.5)

    ax.fill_between(profile_chart['distance'], profile_chart['frenzel_zone_1_60_top'],
                    profile_chart['frenzel_zone_1_60_bottom'], color='red', alpha=.15, linewidth=0)

    ax.fill_between(profile_chart['distance'], profile_chart['relief_arc'], min(profile_chart['relief']), color='darkgreen', alpha=.4)

    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Elevation (m)')

    plt.legend()
    plt.title(
        f'Profile from "{radio_profile.startpoint.name}" {radio_profile.startpoint.latitude} {radio_profile.startpoint.longitude} '
        f'H={radio_profile.startheight} to "{radio_profile.stoppoint.name}" {radio_profile.stoppoint.latitude} '
        f'{radio_profile.stoppoint.longitude}  H={radio_profile.stopheight}\n'
        f'Distance {radio_profile.length / 1000:.2f} km, Frequency {radio_profile.frequency}GHz')

    plt.savefig(cache_dir / filename, dpi=300, format='png')
    plt.close()
    return {'distance': radio_profile.length / 1000,
            'az_a_b': p_a.azimuth(p_b),
            'az_b_a': p_b.azimuth(p_a),
            'a_elevation': p_a.elevation,
            'b_elevation': p_b.elevation,
            'a_height': antenna_a_height,
            'b_height': antenna_b_height,
            'line_of_sight': radio_profile.line_of_sight,
            'visibility_in_0_6_fresnel_zone': radio_profile.visibility_in_0_6_fresnel_zone,
            'expected_signal_strength': radio_profile.expected_signal_strength,
            'filename': filename,
            }


def distance(latitude_a: float, longitude_a: float, latitude_b: float, longitude_b: float) -> dict:
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


def nextpoint(latitude_a: float, longitude_a: float, distance: float, bearing: float) -> dict:
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


def get_elevation_to_db(point_id: int) -> bool:
    with app.app_context():
        site = SiteModel.query.get(point_id)
        p_a = GeoPoint(site.latitude, site.longitude)
        if p_a.elevation is None:
            site.elevation = 0
        else:
            site.elevation = p_a.elevation
        db.session.add(site)
        db.session.commit()
    return {'elevation': p_a.elevation}
