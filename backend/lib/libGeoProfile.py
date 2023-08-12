from lib.srtm import srtm
from lib import GeoPoint

# TODO: create tests


class GeoProfile:
    """ Geo path. Start and end points """

    def __init__(self, startpoint: GeoPoint, stoppoint: GeoPoint):
        self.startpoint = startpoint
        self.stoppoint = stoppoint
        self.length = self.startpoint.distance_to(self.stoppoint)
        # List for relief
        self.relief = list()

    def get_relief(self, incremental: int = 10):
        """ Calculate elevation points on a straight line between start and end.
        """
        distance = 0

        nextpoint = self.startpoint
        self.relief.append((0, srtm.get_elevation_point(nextpoint.latitude, nextpoint.longitude)))

        for i in range(int(self.length // incremental)):
            distance += incremental
            nextpoint = self.startpoint.nextpoint(self.startpoint.azimuth(self.stoppoint), distance)
            elevation = srtm.get_elevation_point(nextpoint.latitude, nextpoint.longitude)

            self.relief.append((distance, elevation))

            # For flat surfaces, it makes no sense to keep all the points.
            # Check: if the three previous points have the same height, then remove the middle one.
            if len(self.relief) > 3 and (self.relief[-1][1] == self.relief[-2][1] and self.relief[-1][1] == self.relief[-3][1]):
                # But check the distance to the third point from the end.
                # For long flat surfaces, you still need to draw a surface (for example, a long stretch of water)
                if distance - self.relief[-3][0] < 500:
                    del self.relief[-2]

        nextpoint = self.stoppoint
        self.relief.append((self.length, srtm.get_elevation_point(nextpoint.latitude, nextpoint.longitude)))

    def get_chart_data(self):
        """ Chart data.
            Returns a list of data points:
            - distance from starting point
            - relief height
        """
        chart_data = {'distance': [], 'relief': []}
        # checking the availability of terrain data. If not, then we calculate.
        if len(self.relief) == 0:
            self.get_relief()

        for point in self.relief:
            distance = point[0]
            elevation = point[1]
            chart_data['distance'].append(distance)
            chart_data['relief'].append(elevation)
        return chart_data
