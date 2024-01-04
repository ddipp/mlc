import matplotlib.pyplot as plt

from lib import GeoPoint, RadioProfile


def radio_profile_graph(tx_power: int, frequency: int, receiver_sensitivity: float,
                        antenna_gain_a: float, latitude_a: float, longitude_a: float, height_a: int,
                        antenna_gain_b: float, latitude_b: float, longitude_b: float, height_b: int, cache_dir: str) -> dict:
    filename = "{0}_{1}_{2}_{3}_{4}_{5}_{6}.png".format(latitude_a, longitude_a, height_a, latitude_b, longitude_b, height_b, frequency)
    p_a = GeoPoint(latitude_a, longitude_a)
    p_b = GeoPoint(latitude_b, longitude_b)

    radio_profile = RadioProfile(p_a, height_a, p_b, height_b, frequency)
    radio_profile.set_radio_parameters(tx_power=tx_power, receiver_sensitivity=receiver_sensitivity,
                                       antenna_gain_a=float(antenna_gain_a), antenna_gain_b=float(antenna_gain_b))
    profile_chart = radio_profile.get_chart_data()
    plt.rcParams["figure.figsize"] = (14, 9)
    fig = plt.figure()
    ax = fig.add_subplot()

    ax.grid(True)
    ax.annotate(f'Antenna gain {radio_profile.antenna_gain_a:.1f} dBm\nHeight {height_a}m',
                xy=(0, profile_chart['los_height'][0]), xycoords='data',
                xytext=(0.1, 0.5), textcoords='axes fraction',
                horizontalalignment='left',
                arrowprops=dict(arrowstyle="simple",
                                fc="0.6", ec="none",
                                connectionstyle="arc3,rad=0.3"),
                bbox=dict(boxstyle="round", fc="1", alpha=0.5))

    ax.annotate(f'Antenna gain {radio_profile.antenna_gain_b:.1f} dBm\nHeight {height_b}m',
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
            label="60% 1 Frenzel zone", color='red', linewidth=0.15, alpha=.15)
    ax.plot(profile_chart['distance'], profile_chart['frenzel_zone_1_60_bottom'], color='red', linewidth=0.15, alpha=.15)

    ax.plot(profile_chart['distance'], profile_chart['frenzel_zone_1_top'], label="1 Frenzel zone", color='lightcoral', linewidth=0.5)
    ax.plot(profile_chart['distance'], profile_chart['frenzel_zone_1_bottom'], color='lightcoral', linewidth=0.5)

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
            'a_height': height_a,
            'b_height': height_b,
            'line_of_sight': radio_profile.line_of_sight,
            'visibility_in_0_6_fresnel_zone': radio_profile.visibility_in_0_6_fresnel_zone,
            'expected_signal_strength': radio_profile.expected_signal_strength,
            'filename': filename,
            }


def profile(tx_power: int, frequency: int, receiver_sensitivity: float,
            antenna_gain_a: float, latitude_a: float, longitude_a: float, height_a: int,
            antenna_gain_b: float, latitude_b: float, longitude_b: float, height_b: int) -> dict:
    p_a = GeoPoint(latitude_a, longitude_a)
    p_a.h = height_a
    p_b = GeoPoint(latitude_b, longitude_b)
    p_b.h = height_b
    radio_profile = RadioProfile(p_a, p_a.h, p_b, p_b.h, frequency)
    radio_profile.set_radio_parameters(tx_power=tx_power, receiver_sensitivity=receiver_sensitivity,
                                       antenna_gain_a=float(antenna_gain_a), antenna_gain_b=float(antenna_gain_b))
    return {'distance': radio_profile.length / 1000,
            'az_a_b': p_a.azimuth(p_b),
            'az_b_a': p_b.azimuth(p_a),
            'a_elevation': p_a.elevation,
            'b_elevation': p_b.elevation,
            'a_height': p_a.h,
            'b_height': p_b.h,
            'line_of_sight': radio_profile.line_of_sight,
            'visibility_in_0_6_fresnel_zone': radio_profile.visibility_in_0_6_fresnel_zone,
            'expected_signal_strength': radio_profile.expected_signal_strength,
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
