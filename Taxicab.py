# Author: Samuel Bennett
# Date: 4/28/2021
# Description: Determines the odometer distance of a taxi from a set of coordinates


class Taxicab:
    """Represents a taxi with coordinates x, y, and odometer"""
    def __init__(self, x_coord, y_coord):
       self.x_coord = x_coord
       self.y_coord = y_coord
       self.odometer = 0

    def get_x_coord(self):
       return self.x_coord

    def get_y_coord(self):
       return self.y_coord

    def move_x(self, x_coord):
        self.x_coord = x_coord
        self.odometer += abs(x_coord)

    def move_y(self, y_coord):
        self.y_coord = y_coord
        self.odometer += abs(y_coord)

    def get_odometer(self):
           return self.odometer

cab = Taxicab(5, -8)
cab.move_x(3)
cab.move_y(-4)
cab.move_x(-1)
print(cab.get_odometer())

