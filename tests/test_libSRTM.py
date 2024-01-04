import os
from lib.srtm import srtm


def test_file_name_for_point():
    assert srtm.file_name_for_point(56.86358, 60.62379) == 'N56E060.hgt'
    assert srtm.file_name_for_point(-56.86358, 60.62379) == 'S57E060.hgt'
    assert srtm.file_name_for_point(-56.86358, -60.62379) == 'S57W061.hgt'
    assert srtm.file_name_for_point(56.86358, -60.62379) == 'N56W061.hgt'
    assert srtm.file_name_for_point(56, 60) == 'N56E060.hgt'
    assert srtm.file_name_for_point(-56, 60) == 'S57E060.hgt'
    assert srtm.file_name_for_point(-56, -60) == 'S57W061.hgt'
    assert srtm.file_name_for_point(56, -60) == 'N56W061.hgt'


def test_get_elevation_point_NW():
    assert srtm.get_elevation_point(1, 31) == 1141
    assert srtm.get_elevation_point(1, 31.99999) == 1062
    assert srtm.get_elevation_point(1.99999, 31.99999) == 1092
    assert srtm.get_elevation_point(1.99999, 31) == 773
    assert srtm.get_elevation_point(1.274309, 31.358084) == 1122
    assert srtm.get_elevation_point(1.115976, 31.087493) == 1116
    assert srtm.get_elevation_point(1.079952, 31.121195) == 1090
    assert srtm.get_elevation_point(1.151424, 30.447990) == 622
    assert srtm.get_elevation_point(1.018542, 30.656552) == 1202
    assert srtm.get_elevation_point(67.579852, 10.776552) is None  # open ocean. There is no SRTM file for these coordinates


def test_get_elevation_point_SW():
    assert srtm.get_elevation_point(-4.00001, 29.00001) == 1632
    assert srtm.get_elevation_point(-4, 29) == 1632
    assert srtm.get_elevation_point(-4.00001, 29.99999) == 1334
    assert srtm.get_elevation_point(-4, 29.99999) == 1334
    assert srtm.get_elevation_point(-4.99999, 29.99999) == 1095
    assert srtm.get_elevation_point(-4.99999, 29) == 1981
    assert srtm.get_elevation_point(-4.106989, 29.105975) == 767
    assert srtm.get_elevation_point(-4.139669, 29.411452) == 767
    assert srtm.get_elevation_point(-4.159174, 29.238954) == 1444
    assert srtm.get_elevation_point(-5.679582, 29.374339) == 767
    assert srtm.get_elevation_point(-5.592160, 29.314274) == 1481


def test_get_elevation_point_NE():
    assert srtm.get_elevation_point(52, -6.00001) == 0
    assert srtm.get_elevation_point(52, -6) == 0
    assert srtm.get_elevation_point(52, -6.99999) == 0
    assert srtm.get_elevation_point(52.99999, -6.99999) == 60
    assert srtm.get_elevation_point(52.99999, -6.00001) == 0
    assert srtm.get_elevation_point(52.99999, -6) == 0
    assert srtm.get_elevation_point(52.966951, -6.465526) == 919
    assert srtm.get_elevation_point(52.959848, -6.336204) == 449
    assert srtm.get_elevation_point(52.968336, -6.183284) == 203
    assert srtm.get_elevation_point(55.841989, -41.038896) is None
    assert srtm.get_elevation_point(43.4375, -2.9125) is None


def test_get_elevation_point_SE():
    assert srtm.get_elevation_point(-3.00001, -79.00001) == 2818
    assert srtm.get_elevation_point(-3, -79) == 2818
    assert srtm.get_elevation_point(-3.00001, -79.99999) == 0
    assert srtm.get_elevation_point(-3, -79.99999) == 0
    assert srtm.get_elevation_point(-3.99999, -79.99999) == 1213
    assert srtm.get_elevation_point(-3.99999, -79.00001) == 2096
    assert srtm.get_elevation_point(-3.99999, -79) == 2096
    assert srtm.get_elevation_point(-3.991163, -79.092340) == 2005
    assert srtm.get_elevation_point(-3.957352, -79.023306) == 1553
    assert srtm.get_elevation_point(-3.991068, -79.015972) == 1507


def test_unpack_zip():
    assert srtm.get_elevation_point(0.1, 72.1) == 0
    assert os.path.exists("data/cache/N00E072.hgt")
    if os.path.exists("data/cache/N00E072.hgt"):
        os.remove("data/cache/N00E072.hgt")
    if os.path.exists("data/cache/N01E030.hgt"):
        os.remove("data/cache/N01E030.hgt")
    if os.path.exists("data/cache/N01E031.hgt"):
        os.remove("data/cache/N01E031.hgt")
    if os.path.exists("data/cache/N43W003.hgt"):
        os.remove("data/cache/N43W003.hgt")
    if os.path.exists("data/cache/N52W007.hgt"):
        os.remove("data/cache/N52W007.hgt")
    if os.path.exists("data/cache/S04W080.hgt"):
        os.remove("data/cache/S04W080.hgt")
    if os.path.exists("data/cache/S05E029.hgt"):
        os.remove("data/cache/S05E029.hgt")
    if os.path.exists("data/cache/S06E029.hgt"):
        os.remove("data/cache/S06E029.hgt")
