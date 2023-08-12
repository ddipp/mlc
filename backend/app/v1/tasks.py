import matplotlib.pyplot as plt

from lib import GeoPoint, GeoProfile, RadioProfile

# TODO: create tests


def radio_profile_check(la_a: float, lo_a: float, h_a: float, la_b: float, lo_b: float, h_b: float, f: float, tx_p: float, r_s: float,
                        a_g_a: float, a_g_b: float):
    p_a = GeoPoint(la_a, lo_a)
    p_b = GeoPoint(la_b, lo_b)
    radio_profile = RadioProfile(p_a, h_a, p_b, h_b, f)
    radio_profile.set_radio_parameters(tx_power=tx_p, receiver_sensitivity=r_s, antenna_gain_a=a_g_a, antenna_gain_b=a_g_b)
    return {"los": radio_profile.line_of_sight, "los_f": radio_profile.visibility_in_fresnel_zone}


def radio_profile_graph(la_a: float, lo_a: float, h_a: float, la_b: float, lo_b: float, h_b: float, f: float, tx_p: float, r_s: float,
                        a_g_a: float, a_g_b: float, cache_dir: str):
    filename = "{0}_{1}_{2}_{3}_{4}_{5}_{6}.png".format(la_a, lo_a, h_a, la_b, lo_b, h_b, f)
    p_a = GeoPoint(la_a, lo_a)
    p_b = GeoPoint(la_b, lo_b)

    distance = p_a.distance_to(p_b) / 1000
    az_a_b = p_a.azimuth(p_b)
    az_b_a = p_b.azimuth(p_a)

    radio_profile = RadioProfile(p_a, h_a, p_b, h_b, f)
    radio_profile.set_radio_parameters(tx_power=tx_p, receiver_sensitivity=r_s, antenna_gain_a=a_g_a, antenna_gain_b=a_g_b)
    profile_chart = radio_profile.get_chart_data()
    plt.rcParams["figure.figsize"] = (14, 9)
    fig = plt.figure()
    ax = fig.add_subplot()

    ax.grid(True)
    ax.annotate(f'Antenna gain {radio_profile.antenna_gain_a:.1f} dBm\nHeight {h_a}m',
                xy=(0, profile_chart['los_height'][0]), xycoords='data',
                xytext=(0.1, 0.5), textcoords='axes fraction',
                horizontalalignment='left',
                arrowprops=dict(arrowstyle="simple",
                                fc="0.6", ec="none",
                                connectionstyle="arc3,rad=0.3"),
                bbox=dict(boxstyle="round", fc="1", alpha=0.5))

    ax.annotate(f'Antenna gain {radio_profile.antenna_gain_b:.1f} dBm\nHeight {h_b}m',
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
    return {'distance': distance,
            'az_a_b': az_a_b,
            'az_b_a': az_b_a,
            'p_a_elevation': p_a.elevation,
            'p_b_elevation': p_b.elevation,
            'filename': filename,
            }


def profile_graph(la_a: float, lo_a: float, la_b: float, lo_b: float, cache_dir: str):
    filename = "{0}_{1}_{2}_{3}.png".format(la_a, lo_a, la_b, lo_b)
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


def nextpoint(latitude_a: float, longitude_a: float, distance: float, bearing: float):
    p_a = GeoPoint(latitude_a, longitude_a)
    p_b = p_a.nextpoint(bearing, distance)
    return {'latitude_b': p_b.latitude,
            'longitude_b': p_b.longitude,
            'p_a_elevation': p_a.elevation,
            'p_b_elevation': p_b.elevation,
            }


def distance(la_a: float, lo_a: float, la_b: float, lo_b: float):
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
