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
