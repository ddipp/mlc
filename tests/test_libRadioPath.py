from lib import GeoPoint, RadioProfile


def test_radio_path1():
    p1 = GeoPoint(1.594837, 31.158936, name='Point1')
    p2 = GeoPoint(1.870223, 30.878149, name='Point2')
    radiopath1 = RadioProfile(startpoint=p1, startheight=20, stoppoint=p2, stopheight=20, frequency=17)
    radiopath1.set_radio_parameters(tx_power=18, receiver_sensitivity=-65, antenna_gain_a=38.1, antenna_gain_b=38.1)
    assert radiopath1.startpoint == p1
    assert radiopath1.stoppoint == p2
    assert radiopath1.frequency == 17
    assert int(radiopath1.length) == 43726
    assert radiopath1.startpoint.elevation == 660
    assert radiopath1.stoppoint.elevation == 624
    assert radiopath1.arc_height(0) == 0
    assert radiopath1.arc_height(radiopath1.length) == 0
    assert int(radiopath1.arc_height(radiopath1.length / 2)) == 37
    assert int(radiopath1.arc_height(radiopath1.length / 4)) == 28
    assert radiopath1.arc_height(radiopath1.length / 4) == radiopath1.arc_height(radiopath1.length / 4 * 3)
    assert radiopath1.line_equation_b == 680
    assert radiopath1.line_equation_k == -0.0008233033589831102
    assert int(radiopath1.los_height(0)) == 680
    assert int(radiopath1.los_height(radiopath1.length)) == 644
    assert int(radiopath1.los_height(radiopath1.length / 2)) == 662
    assert radiopath1.visibility_in_0_6_fresnel_zone is False
    assert radiopath1.line_of_sight is True
    assert len(radiopath1.relief) == 107
    assert round(radiopath1.free_space_loss, 2) == 149.86
    assert radiopath1.expected_signal_strength is None
    assert round(radiopath1.frenzel_zone_size(1, radiopath1.length / 2), 3) == 13.873


def test_radio_path2():
    p1 = GeoPoint(1.594837, 31.158936, name='Point1')
    p2 = GeoPoint(1.870223, 30.878149, name='Point2')
    radiopath1 = RadioProfile(startpoint=p1, startheight=40, stoppoint=p2, stopheight=40, frequency=17)
    radiopath1.set_radio_parameters(tx_power=18, receiver_sensitivity=-65, antenna_gain_a=38.1, antenna_gain_b=38.1)
    assert radiopath1.startpoint == p1
    assert radiopath1.stoppoint == p2
    assert radiopath1.frequency == 17
    assert int(radiopath1.length) == 43726
    assert radiopath1.startpoint.elevation == 660
    assert radiopath1.stoppoint.elevation == 624
    assert radiopath1.arc_height(0) == 0
    assert radiopath1.arc_height(radiopath1.length) == 0
    assert int(radiopath1.arc_height(radiopath1.length / 2)) == 37
    assert int(radiopath1.arc_height(radiopath1.length / 4)) == 28
    assert radiopath1.arc_height(radiopath1.length / 4) == radiopath1.arc_height(radiopath1.length / 4 * 3)
    assert radiopath1.line_equation_b == 700
    assert radiopath1.line_equation_k == -0.0008233033589831102
    assert int(radiopath1.los_height(0)) == 700
    assert int(radiopath1.los_height(radiopath1.length)) == 664
    assert int(radiopath1.los_height(radiopath1.length / 2)) == 682
    assert radiopath1.visibility_in_0_6_fresnel_zone is True
    assert radiopath1.line_of_sight is True
    assert len(radiopath1.relief) == 107
    assert round(radiopath1.free_space_loss, 2) == 149.86
    assert radiopath1.expected_signal_strength == -55.7
    assert round(radiopath1.frenzel_zone_size(1, radiopath1.length / 2), 3) == 13.873


def test_radio_path3():
    p1 = GeoPoint(1.594837, 31.158936, name='Point1')
    p2 = GeoPoint(1.870223, 30.878149, name='Point2')
    radiopath1 = RadioProfile(startpoint=p1, startheight=10, stoppoint=p2, stopheight=10, frequency=36)
    radiopath1.set_radio_parameters(tx_power=18, receiver_sensitivity=-65, antenna_gain_a=38.1, antenna_gain_b=38.1)
    assert radiopath1.startpoint == p1
    assert radiopath1.stoppoint == p2
    assert radiopath1.frequency == 36
    assert int(radiopath1.length) == 43726
    assert radiopath1.startpoint.elevation == 660
    assert radiopath1.stoppoint.elevation == 624
    assert radiopath1.arc_height(0) == 0
    assert radiopath1.arc_height(radiopath1.length) == 0
    assert int(radiopath1.arc_height(radiopath1.length / 2)) == 37
    assert int(radiopath1.arc_height(radiopath1.length / 4)) == 28
    assert radiopath1.arc_height(radiopath1.length / 4) == radiopath1.arc_height(radiopath1.length / 4 * 3)
    assert radiopath1.line_equation_b == 670
    assert radiopath1.line_equation_k == -0.0008233033589831102
    assert int(radiopath1.los_height(0)) == 670
    assert int(radiopath1.los_height(radiopath1.length)) == 634
    assert int(radiopath1.los_height(radiopath1.length / 2)) == 652
    assert radiopath1.line_of_sight is False
    assert radiopath1.visibility_in_0_6_fresnel_zone is False
    assert len(radiopath1.relief) == 107
    assert round(radiopath1.free_space_loss, 2) == 156.38
    assert radiopath1.expected_signal_strength is None
    assert round(radiopath1.frenzel_zone_size(1, radiopath1.length / 2), 3) == 9.533
