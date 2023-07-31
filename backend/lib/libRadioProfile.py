import math as m

from lib.srtm import srtm
from lib import GeoPoint, EARTH_RADIUS


class RadioProfile:
    """ Geo path. Start and end points """

    def __init__(self, startpoint: GeoPoint, startheight: int, stoppoint: GeoPoint, stopheight: int, frequency: int):
        self.startpoint = startpoint
        self.startheight = startheight
        self.stoppoint = stoppoint
        self.stopheight = stopheight
        self.frequency = frequency
        # Radio channel length in meters
        self.length = self.startpoint.distance_to(self.stoppoint)
        # Coefficients for calculating line-of-sight height
        self.line_equation_k = ((self.startpoint.elevation + self.startheight)
                                - (self.stoppoint.elevation + self.stopheight)) / (0 - self.length)
        self.line_equation_b = (self.stoppoint.elevation + self.stopheight) - self.line_equation_k * self.length
        # List for relief
        self.relief = list()
        # Radio parameters
        self.tx_power = None
        self.receiver_sensitivity = None
        self.antenna_gain_a = None
        self.antenna_gain_b = None

    def set_radio_parameters(self, tx_power, receiver_sensitivity, antenna_gain_a, antenna_gain_b):
        self.tx_power = tx_power
        self.receiver_sensitivity = receiver_sensitivity
        self.antenna_gain_a = antenna_gain_a
        self.antenna_gain_b = antenna_gain_b

    def los_height(self, distance: int) -> float:
        """ Calculates the height (in meters) of the line of sight
            above a straight line at a given distance (in meters)
            between the start and end points of the path
            (taking into account the height of the antenna suspension).
        """
        return self.line_equation_k * distance + self.line_equation_b

    def arc_height(self, distance: int) -> float:
        """ The height of the planet's arc at a given distance (in meters) from the start of the path
        """
        a = (m.pi - 2 * m.acos(self.length / (2 * EARTH_RADIUS))) / 2
        t = -1 + distance / (self.length / 2)
        h = EARTH_RADIUS * (m.sqrt((1 - (t**2) * (m.sin(a)**2))) - m.cos(a))
        return h

    def frenzel_zone_size(self, zone_number: int, distance: int) -> float:
        # Fresnel zone size
        d1 = distance / 1000
        d2 = int(self.length - distance) / 1000
        r1 = 17.3 * m.sqrt((d1 * d2) / (self.frequency * (d1 + d2)))
        return r1 * m.sqrt(zone_number)

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
            - the height of the relief, taking into account the curvature of the planet
            - line of sight height
            - height of the first fresnel zone
            - height 60% of the first Fresnel zone
        """
        chart_data = {'distance': [], 'relief': [], 'relief_arc': [], 'los_height': [],
                      'frenzel_zone_1_top': [], 'frenzel_zone_1_bottom': [],
                      'frenzel_zone_1_60_top': [], 'frenzel_zone_1_60_bottom': []}
        # checking the availability of terrain data. If not, then we calculate.
        if len(self.relief) == 0:
            self.get_relief()

        for point in self.relief:
            distance = point[0]
            elevation = point[1]
            arc_height = self.arc_height(distance)
            los_height = self.los_height(distance)
            frenzel_zone_1 = self.frenzel_zone_size(1, distance)
            chart_data['distance'].append(distance)
            chart_data['relief'].append(elevation)
            chart_data['relief_arc'].append(elevation + arc_height)
            chart_data['los_height'].append(los_height)
            chart_data['frenzel_zone_1_top'].append(los_height + frenzel_zone_1)
            chart_data['frenzel_zone_1_bottom'].append(los_height - frenzel_zone_1)
            chart_data['frenzel_zone_1_60_top'].append(los_height + frenzel_zone_1 * 0.6)
            chart_data['frenzel_zone_1_60_bottom'].append(los_height - frenzel_zone_1 * 0.6)
        return chart_data

    @property
    def line_of_sight(self) -> bool:
        """ having a direct line of sight.
            If there are obstacles on the way between points (considering antenna heights),
            then False is returned, otherwise True.
        """
        # checking the availability of terrain data. If not, then we calculate.
        if len(self.relief) == 0:
            self.get_relief()

        # Iterate over the heights and compare with the height of the line of sight at that point.
        for point in self.relief:
            distance = point[0]
            elevation = point[1]
            los_height = self.los_height(distance)
            arc_height = self.arc_height(distance)
            # Compare line of sight height and surface height + planet curvature
            if los_height < elevation + arc_height:
                return False

        return True

    @property
    def visibility_in_fresnel_zone(self) -> bool:
        """ the presence of visibility in the 60% fresnel zones.
            If there are obstacles on the way between points (considering antenna heights),
            then False is returned, otherwise True.
        """
        # checking the availability of terrain data. If not, then we calculate.
        if len(self.relief) == 0:
            self.get_relief()

        for point in self.relief:
            distance = point[0]
            elevation = point[1]
            los_height = self.los_height(distance)
            arc_height = self.arc_height(distance)
            frenzel_zone = self.frenzel_zone_size(1, distance) * 0.6
            # Compare line of sight height and surface height + planet curvature
            if los_height - frenzel_zone < elevation + arc_height:
                return False

        return True

    @property
    def free_space_loss(self):
        """ Calculating free space loss
            ref: HANDBOOK – DIGITAL RADIO-RELAY SYSTEMS (R-HDB-24-1996-PDF-E.pdf)
            formula (4.1.1-1)
        """
        return 92.44 + 20 * m.log10(self.frequency) + 20 * m.log10(self.length / 1000)

    @property
    def expected_signal_strength(self):
        if self.line_of_sight is False or self.visibility_in_fresnel_zone is False:
            ess = None
        else:
            ess = self.tx_power + self.antenna_gain_a + self.antenna_gain_b - self.free_space_loss
            ess = round(ess, 2)
        return ess
