import bz2
from pathlib import Path

try:
    from ..productionconfig import SRTM3_DIR
except ImportError:
    from ..config import SRTM3_DIR


cache_dir = Path.cwd() / 'data' / 'cache'
srtm3_dir = Path(SRTM3_DIR)


def file_name_for_point(latitude: float, longitude: float) -> str:
    """
    For the specified coordinates, returns the name of the SRTM3 file
    """
    north_south = 'N' if latitude >= 0 else 'S'
    east_west = 'E' if longitude >= 0 else 'W'
    # The coordinates are converted so that the numbers are truncated to integers.
    # However, since the reference point in the HGT file starts from the lower left corner,
    # one degree must be subtracted for the negative coordinate.
    # (12.123 -> 12, -12.123 -> -13, -12 -> -13)
    latitude = latitude - (1 if latitude < 0 else 0)
    longitude = longitude - (1 if longitude < 0 else 0)
    latitude = abs(int(latitude))
    longitude = abs(int(longitude))
    return '{0}{1}{2}{3}.hgt'.format(north_south, str(latitude).zfill(2),
                                     east_west, str(longitude).zfill(3))


def hgt_file(latitude: float, longitude: float) -> Path:
    """
    For the specified coordinates, returns the name of the SRTM3 file.
    If this file is not in the cache folder, then we look for the packed file in the srtm3 folder, unpack it and return the name.
    If no file exists for the given coordinates, then return None.
    """
    hgt_file_name = file_name_for_point(latitude, longitude)
    # Checking if the file is in the cache.
    cache_hgt_file_name = cache_dir / hgt_file_name
    if not cache_hgt_file_name.exists():
        # Checking if the zip file exists
        bz2_hgt_file_name = (srtm3_dir / hgt_file_name[0:3] / hgt_file_name).with_suffix('.hgt.bz2')
        # If no file exists for the given coordinates, then return None.
        if bz2_hgt_file_name.exists():
            with bz2.open(bz2_hgt_file_name, "rb") as cf:
                open(cache_hgt_file_name, 'wb').write(cf.read())
            return cache_hgt_file_name
        # Else unpack and return filename
        else:
            return None
    else:
        return cache_hgt_file_name


def read_elevation(file, latitude: float, longitude: float) -> int:
    # For the northern hemisphere
    if latitude > 0:
        i = 1200 - int(round((abs(latitude) - abs(int(latitude))) * (1201 - 1), 0))
    # For the southern hemisphere
    else:
        i = int(round((abs(latitude) - abs(int(latitude))) * (1201 - 1), 0))
    # For the Eastern Hemisphere
    if longitude > 0:
        j = int(round((abs(longitude) - abs(int(longitude))) * (1201 - 1), 0))
    # For the Western Hemisphere
    else:
        j = 1200 - int(round((abs(longitude) - abs(int(longitude))) * (1201 - 1), 0))
    pos = (i * 1201) + j
    file.seek(pos * 2)
    val = int.from_bytes(file.read(2), byteorder="big", signed=True)
    if val == -32768:
        return None
    return val


opened_srtm_file = None
f = open("/dev/null", 'rb')


def get_elevation_point(latitude: float, longitude: float) -> int:
    """ For the given coordinates, returns the height of the ground level above sea level
        (or None if there is no data).
        To get the height of one point, we read only one byte from the file.
    """
    global opened_srtm_file, f
    srtm_file = hgt_file(latitude, longitude)
    if srtm_file is None:
        return None

    if opened_srtm_file != srtm_file:
        f.close()
        f = open(srtm_file, "rb")
        opened_srtm_file = srtm_file

    return read_elevation(f, latitude, longitude)


def get_coordinates_from_point():
    pass

# def get_elevation_point(latitude: float, longitude: float) -> int:
#     SAMPLES = 1201
#     srtm_file = hgt_file(latitude, longitude)
#     if srtm_file is None:
#         return None
#     with open(srtm_file, 'rb') as hgt_data:
#         elevations = np.fromfile(hgt_data, np.dtype('>i2'), SAMPLES * SAMPLES).reshape((SAMPLES, SAMPLES))
#         # For the northern hemisphere
#         if latitude > 0:
#             i = 1200 - int(round((abs(latitude) - abs(int(latitude))) * (1201 - 1), 0))
#         # For the southern hemisphere
#         else:
#             i = int(round((abs(latitude) - abs(int(latitude))) * (1201 - 1), 0))

#         # For the Eastern Hemisphere
#         if longitude > 0:
#             j = int(round((abs(longitude) - abs(int(longitude))) * (1201 - 1), 0))
#         # For the Western Hemisphere
#         else:
#             j = 1200 - int(round((abs(longitude) - abs(int(longitude))) * (1201 - 1), 0))

#     return elevations[i, j].astype(int)
