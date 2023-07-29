from lib import GeoPoint


def test_geo_point():
    p1 = GeoPoint(1.566691, 31.125062, name='Point1', elevation=902)
    assert p1.latitude == 1.566691
    assert p1.longitude == 31.125062
    assert p1.elevation == 902
    assert p1.rlongitude == 0.5432348117873713
    assert p1.rlatitude == 0.027343916311362484
    assert p1.name == 'Point1'
    assert p1.x == 5452578.415637233
    assert p1.y == 3292459.3907471513
    assert p1.z == 174211.28990068485
    p2 = GeoPoint(1.571950, 31.128231, name='Point1')
    assert p2.elevation == 811
    p3 = GeoPoint(1.615452, 31.141755, name='Point1')
    assert p3.elevation == 615
    p4 = GeoPoint(1.294512, 30.423211, name='Point1')
    assert p4.elevation == 615
    p5 = GeoPoint(1.661187, 30.600927, name='Point1')
    assert p5.elevation == 2161
    p6 = GeoPoint(0, 0, name='00')
    assert p6.elevation is None
    assert p6.x == 6371009
    assert p6.y == 0
    assert p6.z == 0


def test_geo_diatsnce():
    p1 = GeoPoint(90, 0, name='N', elevation=0)
    p2 = GeoPoint(-90, 0, name='S', elevation=0)
    assert p1.distance_to(p2) == 12742018
    assert p1.arc_distance_to(p2) == 20015115.070354454
    p3 = GeoPoint(0, 0, name='G', elevation=0)
    p4 = GeoPoint(0, 180, name='g', elevation=0)
    assert p3.distance_to(p4) == 12742018
    assert p3.arc_distance_to(p4) == 20015115.070354454
    p5 = GeoPoint(1.053820, 30.072736, name='Y')
    p6 = GeoPoint(1.074309, 31.058084, name='S')
    assert p5.distance_to(p6) == 109586.60471246624
    assert p5.arc_distance_to(p6) == 109570.64671368369
    p7 = GeoPoint(1.053820, 30.072736, name='Y', elevation=0)
    p8 = GeoPoint(1.074309, 31.058084, name='S', elevation=0)
    assert p7.distance_to(p8) == 109569.29634178957
    assert p7.arc_distance_to(p8) == 109570.64671368369
    p9 = GeoPoint(1.661187, 30.600927, name='Peak')
    p10 = GeoPoint(1.661187, 30.600927, name='Sea level', elevation=0)
    assert int(p9.distance_to(p10)) == 2160
    assert p9.arc_distance_to(p10) == 0.0


def test_geo_azimuth():
    p1 = GeoPoint(1.153820, 30.472736)
    p2 = GeoPoint(1.274309, 31.358084)
    assert p1.azimuth(p2) == 82.23915534111224
    assert p2.azimuth(p1) == 262.2579143339059
    p3 = GeoPoint(0, 0, elevation=0)
    p4 = GeoPoint(0, 20, elevation=0)
    assert p3.azimuth(p4) == 90
    assert p4.azimuth(p3) == 270
    p5 = GeoPoint(54.9132538, 34.3426619, elevation=0)
    p6 = GeoPoint(55.9132538, 34.3426619, elevation=0)
    assert p5.azimuth(p6) == 0.0
    assert p6.azimuth(p5) == 180
    p7 = GeoPoint(0, 0, elevation=0)
    p8 = GeoPoint(1, 1, elevation=0)
    assert p7.azimuth(p8) == 44.99563645534485
    assert p8.azimuth(p7) == 225.00436354465515
    p7 = GeoPoint(0, 0, elevation=0)
    p8 = GeoPoint(90, 0, elevation=0)
    assert p7.azimuth(p8) == 0
    assert p8.azimuth(p7) == 180


def test_geo_nextpoint():
    p1 = GeoPoint(1.153820, 30.472736)
    p2 = p1.nextpoint(azimuth=82.23915534111224, distance=80000)
    assert (p2.latitude, p2.longitude) == (1.2508824502322442, 31.18577189492941)
    assert int(p1.distance_to(p2)) == 80012
    p3 = GeoPoint(0, 0, name='N')
    p4 = p3.nextpoint(azimuth=-90, distance=20015115.070354454)
    assert (p4.latitude, p4.longitude) == (4.296495291499103e-31, -180)
    p5 = GeoPoint(0, 0, name='N')
    p6 = p5.nextpoint(azimuth=90, distance=20015115.070354454 / 2)
    assert (p6.latitude, p6.longitude) == (3.508354649267438e-15, 90)


def test_geo_to_json():
    p1 = GeoPoint(1.153820, 30.472736)
    assert p1.to_json() == '{"latitude": 1.15382, "longitude": 30.472736, "name": "", "elevation": 622}'
    p2 = GeoPoint(1.566691, 31.125062, name='Point1', elevation=902)
    assert p2.to_json() == '{"latitude": 1.566691, "longitude": 31.125062, "name": "Point1", "elevation": 902}'


def test_geo_str():
    p1 = GeoPoint(1.153820, 30.472736)
    assert p1.__str__() == "GeoPoint name \t1.15382, 30.472736, 622"
    p2 = GeoPoint(1.566691, 31.125062, name='Point1', elevation=902)
    assert p2.__str__() == "GeoPoint name Point1\t1.566691, 31.125062, 902"
