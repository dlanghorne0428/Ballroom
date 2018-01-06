""" The Position Module contains a Position() class and NO_MOVEMENT constant"""
import copy
import math

class Position():
    """
    The Position() class implements a position in 2-D space, representing
    an x-coordinate, y-coordinate, and an angle.
    """

    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0

    def copy(self):
        return copy.deepcopy(self)

    def set(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def adjust(self, x, y, angle):
        """ modify the current position by the given amounts """
        self.x += x
        self.y += y
        self.angle += angle
        if self.angle > 360:
            self.angle -= 360
        elif self.angle <= -360:
            self.angle += 360

    def offset_by(self, x_dist, y_dist, rotation):
        """
        Create a new position based on the current position.
        The x_dist and y_dist offsets are assuming the current position is
        at 0 degrees of rotation.
        """
        new_pos = Position()
        new_pos.x = (self.x
                  + x_dist * math.sin(math.radians(self.angle+90))
                  + y_dist * math.cos(math.radians(self.angle+90)))
        new_pos.y = (self.y
                  + x_dist * math.sin(math.radians(self.angle))
                  + y_dist * math.cos(math.radians(self.angle)))
        new_pos.angle = self.angle + rotation
        if new_pos.angle > 360:
            new_pos.angle -= 360
        elif new_pos.angle < -360:
            new_pos_angle += 360

        return new_pos

    def print(self):
        print("(", round(self.x,2),",", round(self.y,2),",", round(self.angle,2),")",end="\t")

NO_MOVEMENT = Position()
