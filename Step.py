from enum import IntEnum
import arcade
import Position
import math

class Foot(IntEnum):
    LEFT = 0
    RIGHT = 1
    BOTH = 2

class Step():

    feet_spread_distance = 80

    def __init__(self, foot, duration, pre_step_pivot=0, rotation=0):
        self.duration = duration
        self.foot = foot
        self.pre_step_pivot = pre_step_pivot
        self.rotation = rotation

    def set_spread(distance):
        feet_spread_distance = distance

    def get_pre_step_pivot(self, foot):
        if foot == self.foot:
            return self.pre_step_pivot
        else:
            return 0

    def update_vector_setup(self, foot, current_pos):
        if foot == Foot.LEFT:
            self.reference = current_pos[Foot.RIGHT].copy()
            self.start_pos = current_pos[Foot.LEFT].copy()
            self.spread = -Step.feet_spread_distance
        else:
            self.reference = current_pos[Foot.LEFT].copy()
            self.start_pos = current_pos[Foot.RIGHT].copy()
            self.spread = Step.feet_spread_distance

    def calc_new_position(self):
        return self.start_pos

    def update_vector_calc(self):
        upd_vec = Position.Position()
        upd_vec.x = (self.new_pos.x - self.start_pos.x) / self.duration
        upd_vec.y = (self.new_pos.y - self.start_pos.y) / self.duration
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

    def __init__(self, foot, stride, duration, pre_step_pivot = 0, rotation = 0):
        super().__init__(foot, duration, pre_step_pivot, rotation)
        self.stride = stride

    def calc_new_position(self):
        new_pos = Position.Position()
        self.reference.angle += self.pre_step_pivot   # HACK - is this what I want?
        new_pos.x = (self.reference.x
                  + self.spread * math.sin(math.radians(self.reference.angle+90))
                  + self.stride * math.cos(math.radians(self.reference.angle+90)))
        new_pos.y = (self.reference.y
                  + self.spread * math.sin(math.radians(self.reference.angle))
                  + self.stride * math.cos(math.radians(self.reference.angle)))
        new_pos.angle = self.reference.angle + self.rotation

        return new_pos


class Backward(Forward):

    def __init__(self, foot, stride, duration, pre_step_pivot = 0, rotation = 0):
        super().__init__(foot, stride, duration, pre_step_pivot, rotation)
        self.stride = -stride

class Side(Step):

    def __init__(self, foot, stride, duration, pre_step_pivot = 0, rotation=0):
        super().__init__(foot, duration, pre_step_pivot, rotation)
        self.stride = stride

    def calc_new_position(self):
        new_pos = Position.Position()
        self.reference.angle += self.pre_step_pivot   # HACK - is this what I want?        
        new_pos.x = (self.reference.x 
                  + (self.stride + self.spread) * math.sin(math.radians(self.reference.angle+90)))
        new_pos.y = (self.reference.y 
                  + (self.stride + self.spread) * math.sin(math.radians(self.reference.angle)))
        new_pos.angle = self.reference.angle + self.rotation

        return new_pos

class Close(Step):

    def __init__(self, foot, duration):
        super().__init__(foot, duration)

    def calc_new_position(self):
        new_pos = Position.Position()
        new_pos.x = self.reference.x + self.spread * math.sin(math.radians(self.reference.angle+90))
        new_pos.y = self.reference.y + self.spread * math.sin(math.radians(self.reference.angle))
        new_pos.angle = self.reference.angle

        return new_pos

class Follow(Step):

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
        x_offset = 40
        y_offset = 160
        angle_offset = 180
        new_pos = Position.Position()
        new_pos.x = (self.reference.x
                  + x_offset * math.sin(math.radians(self.reference.angle+90))
                  + y_offset * math.cos(math.radians(self.reference.angle+90)))
        new_pos.y = (self.reference.y
                  + x_offset * math.sin(math.radians(self.reference.angle))
                  + y_offset * math.cos(math.radians(self.reference.angle)))
        new_pos.angle = self.reference.angle + angle_offset

        return new_pos



# class Complex_Step(Step):
#
#     def __init__(self, foot, x_dist, y_dist, rotation, duration, x_dist_r = 0, y_dist_r = 0, rot_2 = 0):
#         super().__init__(foot, duration)
#         if foot == Foot.LEFT:
#             self.x_distance_left = x_dist
#             self.y_distance_left = y_dist
#             self.rotation_angle_left = rotation
#             self.x_distance_right = 0
#             self.y_distance_right = 0
#             self.rotation_angle_right = 0
#         elif foot == Foot.RIGHT:
#             self.x_distance_right = x_dist
#             self.y_distance_right = y_dist
#             self.rotation_angle_right = rotation
#             self.x_distance_left = 0
#             self.y_distance_left = 0
#             self.rotation_angle_left = 0
#         else:
#             self.x_distance_left = x_dist
#             self.y_distance_left = y_dist
#             self.rotation_angle_left = rotation
#             self.x_distance_right = x_dist_r
#             self.y_distance_right = y_dist_r
#             self.rotation_angle_right = rot_r
#
#     def get_update_vector(self, foot, current_pos):
#         upd_vec = Position.Position()
#         if foot == self.foot:
#             if foot == Foot.LEFT:
#                 upd_vec.x = self.x_distance_left / self.duration
#                 y_offset = (current_pos[Foot.RIGHT].y - current_pos[Foot.LEFT].y) * math.cos(math.radians(current_pos[Foot.LEFT].angle))
#                 upd_vec.y = (self.y_distance_left + y_offset) / self.duration
#                 upd_vec.angle = self.rotation_angle_left / self.duration
#             else:
#                 upd_vec.x = self.x_distance_right / self.duration
#                 y_offset = (current_pos[Foot.LEFT].y - current_pos[Foot.RIGHT].y) * math.cos(math.radians(current_pos[Foot.RIGHT].angle))
#                 upd_vec.y = (self.y_distance_right + y_offset) / self.duration
#                 upd_vec.angle = self.rotation_angle_right / self.duration
#
#         return upd_vec
