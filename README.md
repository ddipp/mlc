[![pytest](https://github.com/ddipp/mlc/actions/workflows/pytest.yml/badge.svg)](https://github.com/ddipp/mlc/actions/workflows/pytest.yml) [![codecov](https://codecov.io/gh/ddipp/mlc/graph/badge.svg?token=PCTYG4XGKX)](https://codecov.io/gh/ddipp/mlc)
# microwave link calculator
## SRTM data
To work with terrain data, you need SRTM data.

```python3
from lib.srtm import srtm

assert srtm.get_elevation_point(1.079952, 31.121195) == 1090
assert srtm.get_elevation_point(1.151424, 30.447990) == 622
assert srtm.get_elevation_point(1.018542, 30.656552) == 1202
assert srtm.get_elevation_point(67.579852, 10.776552) is None  # open ocean. There is no SRTM file for these coordinates
assert srtm.get_elevation_point(-3.00001, -79.99999) == 0  # For coastal waters, returns 0
```
## GeoPoint class
The essence of a geographic point.
The coordinates of the point and optionally the height above sea level are set. If the height is not specified, then the height is taken from the SRTM3 data.
Geographic point methods:
- calculation of azimuth between two points
- calculates the coordinates of the next point in the given azimuth and distance.
- calculation of the distance between two points in meters in a straight line.
- calculation of the distance between two points in meters on the surface of the planet.
- each point has properties - coordinates in the x, y, z format with the origin at the center of the planet.

```python3
from lib import GeoPoint

p1 = GeoPoint(43.350183, 42.451874, name='Elbrus')
p2 = GeoPoint(43.350183, 42.451874, name='Elbrus sea level', elevation=0)
assert p1.distance_to(p2) == 5518.999999999588
assert p1.arc_distance_to(p2) == 0.0

p1 = GeoPoint(90, 0, name='N')
p2 = GeoPoint(-90, 0, name='S')
assert p1.distance_to(p2) == 12744717.0
assert p1.arc_distance_to(p2) == 20015115.070354454

p3 = GeoPoint(0, 0, name='00')
assert p3.elevation is None  # This point is in the ocean
assert p3.x == 6371009
assert p3.y == 0
assert p3.z == 0

p4 = GeoPoint(0, 0)
p5 = GeoPoint(1, 1)
assert p4.azimuth(p5) == 44.99563645534485
assert p5.azimuth(p4) == 225.00436354465515

p6 = GeoPoint(54.9132538, 34.3426619)
p7 = p6.nextpoint(azimuth=90, distance=500)
assert (p7.latitude, p7.longitude) == (54.913253548816705, 34.350484580324036)
```
## RadioProfile class
```python3
from lib import GeoPoint, RadioProfile
# Set the start and end points of the radio profile
p1 = GeoPoint(1.594837, 31.158936, name='Point1')
p2 = GeoPoint(1.870223, 30.878149, name='Point2')
# Set a radio profile indicating antenna heights and radio frequencies
radiopath1 = RadioProfile(startpoint=p1, startheight=40, stoppoint=p2, stopheight=40, frequency=17)
# Set antenna gains (dB), transmitter power (dBm), receiver sensitivity (dBm)
radiopath1.set_radio_parameters(tx_power=18, receiver_sensitivity=-65, antenna_gain_a=38.1, antenna_gain_b=38.1)
assert int(radiopath1.length) == 43726
assert radiopath1.startpoint.elevation == 660
assert radiopath1.stoppoint.elevation == 624
# the presence of visibility in the 60% fresnel zones. If there are obstacles on the way between points (considering antennas heights), then False is returned, otherwise True.
assert radiopath1.visibility_in_0_6_fresnel_zone is True
# if there are obstacles on the way between points (considering antennas heights), then False is returned, otherwise True.
assert radiopath1.line_of_sight is True
assert round(radiopath1.free_space_loss, 2) == 149.86
assert radiopath1.expected_signal_strength == -55.7
```
