from lib import GeoPoint, GeoPath


class GeoProfile(GeoPath):
    """ docstring for GeoPath
    """

    def __init__(self, startpoint: GeoPoint, stoppoint: GeoPoint):
        super().__init__(startpoint, stoppoint)

    def get_chart_data(self):
        """ Chart data.
            Returns a list of data points:
            - distance from starting point
            - relief height
            - the height of the relief, taking into account the curvature of the planet
        """
        chart_data = {'distance': [], 'relief': [], 'relief_arc': []}
        # checking the availability of terrain data. If not, then we calculate.
        if len(self.relief) == 0:
            self.get_relief()

        for point in self.relief:
            distance = point[0]
            elevation = point[1]
            chart_data['distance'].append(distance)
            chart_data['relief'].append(elevation)
        return chart_data
