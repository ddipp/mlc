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
