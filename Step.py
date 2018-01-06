"""
The Step module contains the following classes:
- A Foot class to specify which foot is moving
- A Step base class
- Several derived classes for basic steps:
    - Forward
    - Backward
    - Side
    - Close (for closing the feet)
    - Follow (move based on leader's step)
    - Two D (a general step)
"""
from enum import IntEnum
import arcade
import Position

class Foot(IntEnum):
    """ A simple class to enumerate either foot or both"""
    LEFT = 0
    RIGHT = 1
    BOTH = 2

class Step():
    """
    This is the base class for all Steps.
    An object of the base class will not change the foot position.
    This is useful for steps that replace weight onto the other foot.
    """

    feet_spread_distance = 75    #TODO this should come from the Dance

    def __init__(self, foot, duration, pre_step_pivot=0, rotation=0):
        """
        Initialize the class, specify which foot and duration in seconds.
        Optionally specify a pre step pivot angle and rotation angle.
        """
        self.duration = duration
        self.foot = foot
        self.pre_step_pivot = pre_step_pivot
        self.rotation = rotation

    def set_spread(distance):
        feet_spread_distance = distance

    def update_vector_setup(self, foot, current_pos):
        """
        this function initializes the following instance variables:
        - the start_pos is the position of the foot that will be moving
        - the reference is the position of the opposite Foot
        - the spread is the x distance from the other foot, in closed dance position.
        """
        if foot == Foot.LEFT:
            self.reference = current_pos[Foot.RIGHT].copy()
            self.start_pos = current_pos[Foot.LEFT].copy()
            self.spread = -Step.feet_spread_distance
        else:
            self.reference = current_pos[Foot.LEFT].copy()
            self.start_pos = current_pos[Foot.RIGHT].copy()
            self.spread = Step.feet_spread_distance

    def calc_new_position(self):
        """
        The base class simply returns the start pos as the new position.
        Derived Step classes will override this method.
        """
        return self.start_pos

    def update_vector_calc(self):
        """
        This method returns a position vector, where;
        - the x and y values are in pixels per second
        - the angle value is in degrees per second
        """
        upd_vec = Position.Position()
        upd_vec.x = (self.new_pos.x - self.start_pos.x) / self.duration
        upd_vec.y = (self.new_pos.y - self.start_pos.y) / self.duration
        if self.new_pos.angle - self.start_pos.angle >= 180.0:
            print("large positive angle change")
            upd_vec.angle = (self.new_pos.angle - 360.0 - self.start_pos.angle) / self.duration
        elif self.new_pos.angle - self.start_pos.angle <= -180.0:
            print("large negative angle change")
            upd_vec.angle = (self.new_pos.angle + 360.0 - self.start_pos.angle) / self.duration
        else:
            upd_vec.angle = (self.new_pos.angle - self.start_pos.angle) / self.duration
        print(type(self), self.foot, self.start_pos.print(), self.new_pos.print())
        return upd_vec

    def get_update_vector(self, foot, dancer):
        if foot == self.foot:
            self.update_vector_setup(foot, dancer.position)
            self.new_pos = self.calc_new_position()
            dancer.set_next_pos(foot, self.new_pos)
            return self.update_vector_calc()
        else:
            return Position.NO_MOVEMENT

class Forward(Step):
    """
    The Forward() class derives from Step()
    The additional parameter is stride, which is in pixels.
    The new position for the specified foot is that number of pixels in front
    of the dancer's other foot.
    """

    def __init__(self, foot, stride, duration, pre_step_pivot = 0, rotation = 0):
        super().__init__(foot, duration, pre_step_pivot, rotation)
        self.stride = stride

    def calc_new_position(self):
        self.reference.angle += self.pre_step_pivot   # HACK - is this what I want?
        return self.reference.offset_by(self.spread, self.stride, self.rotation)


class Backward(Forward):
    """
    The Backward() class derives from Forward()
    The sign of the stride parameter is inverted.
    Stepping backward by an amount is the same as stepping forward by the negative of that amount.
    """
    def __init__(self, foot, stride, duration, pre_step_pivot = 0, rotation = 0):
        super().__init__(foot, stride, duration, pre_step_pivot, rotation)
        self.stride = -stride


class Side(Step):
    """
    The Side() class derives from Step()
    The additional parameter is stride, which is in pixels.
    The new position for the specified foot is that number of pixels across from
    the dancer's other foot, plus the spread distance between the feet.
    """

    def __init__(self, foot, stride, duration, pre_step_pivot = 0, rotation=0):
        super().__init__(foot, duration, pre_step_pivot, rotation)
        if foot == Foot.LEFT:
            self.stride = -stride    # left offsets are negative
        else:
            self.stride = stride

    def calc_new_position(self):
        self.reference.angle += self.pre_step_pivot   # HACK - is this what I want?
        return self.reference.offset_by(self.stride + self.spread, 0, self.rotation)


class Close(Step):
    """
    The Close() class derives from Step()
    The new position returns the specified foot to closed dance position,
    based on the current position of the dancer's other foot.
    """

    def __init__(self, foot, duration):
        super().__init__(foot, duration)

    def calc_new_position(self):
        return self.reference.offset_by(self.spread, 0, 0)

class Follow(Step):
    """
    The Follow() class derives from Step()
    The new position is based on the partner's foot, assuming a closed dance postion.
    """
    def __init__(self, foot, duration):
        super().__init__(foot, duration)

    def get_update_vector(self, foot, dancer):
        if foot == self.foot:
            self.start_pos = dancer.position[foot].copy()
            # determine where the leader's foot is going to be
            if foot == Foot.LEFT:
                self.reference = dancer.leader.next_pos[Foot.RIGHT].copy()
            else:
                self.reference = dancer.leader.next_pos[Foot.LEFT].copy()

            self.new_pos = self.calc_new_position()
            dancer.set_next_pos(foot, self.new_pos)
            return self.update_vector_calc()
        else:
            return Position.NO_MOVEMENT

    # this can probably be a general routine in the position class
    def calc_new_position(self):
        x_offset = 40       # these should come from the Dance
        y_offset = 140
        angle_offset = 180
        return self.reference.offset_by(x_offset, y_offset, angle_offset)



class Two_D(Step):
    """
    The Two_D() class derives from Step()
    It is a combination of Forward() and Side(), as the new foot position is
    based on the current position of the dancer's other foot.
    Offsets are provided in both x and y directions
    """
    def __init__(self, foot, x_dist, y_dist, duration, pre_step_pivot = 0, rotation = 0):
        super().__init__(foot, duration, pre_step_pivot, rotation)
        if foot == Foot.LEFT:
            self.x_dist = -x_dist
        else:
            self.x_dist = x_dist
        self.y_dist = y_dist

    def calc_new_position(self):
        self.reference.angle += self.pre_step_pivot   # HACK - is this what I want?
        return self.reference.offset_by(self.x_dist + self.spread, self.y_dist, self.rotation)
