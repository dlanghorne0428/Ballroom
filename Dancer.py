""" The Dancer module declares a class for a single Dancer."""
import arcade
import math

from Step import Foot
import Position



class Dancer():
    """
    The Dancer() class defines the state of a given dancer.
    If the dancer is the follower, a reference to the leader must be passed in.
    """

    def __init__(self, leader=None):
        """ initialize the dancer. """
        # the current position of the dancer's feet
        self.position = [Position.Position(), Position.Position()]

        # the update vector of the dancer's feet. in pixels per second and degrees per second
        self.delta_pos = [Position.Position(), Position.Position()]

        # the position of the dancer's feet at the end of the next step
        self.next_pos = [Position.Position(), Position.Position()]

        # the texture images to draw for the dancer's feet.
        self.free_foot_texture = [None, None]
        self.supporting_foot_texture = [None, None]

        # indicate what foot will move next
        self.free_foot = None

        # a reference to the leader. If this dancer is the leader, the variable is set to None
        self.leader = leader

    def load_free_foot_texture(self, foot, filename):
        self.free_foot_texture[foot] = arcade.load_texture(filename)

    def load_supporting_foot_texture(self, foot, filename):
        self.supporting_foot_texture[foot] = arcade.load_texture(filename)

    def set_free_foot(self, foot):
        self.free_foot = foot

    def set_position (self, foot, x, y, angle):
        self.position[foot].set(x, y, angle)

    def set_delta_pos(self, foot, vector):
        self.delta_pos[foot].set(vector.x, vector.y, vector.angle)

    def set_next_pos(self, foot, pos):
        self.next_pos[foot].set(pos.x, pos.y, pos.angle)

    def complete_current_step(self):
        """ force the dancer's position to the end of the current step."""
        if self.free_foot == Foot.LEFT:
            self.position[Foot.LEFT] = self.next_pos[Foot.LEFT].copy()
        elif self.free_foot == Foot.RIGHT:
            self.position[Foot.RIGHT] = self.next_pos[Foot.RIGHT].copy()

    def pivot(self, foot, rotation):
        """ modify the angle of the given foot before the next step"""
        if self.free_foot == foot:
            self.position[foot].adjust(0, 0, rotation)

    def update(self, delta_time):
        """
        Modify the position of the dancer's feet based on the delta_pos vector and the delta_time.
        Only one of the feet will move at a time (except for a lift)
        """
        for foot in range(Foot.BOTH):
            self.position[foot].adjust(self.delta_pos[foot].x * delta_time,
                                       self.delta_pos[foot].y * delta_time,
                                       self.delta_pos[foot].angle * delta_time)

    def draw(self):
        """ select the applicable textures based on free foot and draw them at the current position"""
        if self.free_foot == Foot.LEFT:
            left_tex = self.free_foot_texture[Foot.LEFT]
            right_tex = self.supporting_foot_texture[Foot.RIGHT]
        elif self.free_foot == Foot.RIGHT:
            right_tex = self.free_foot_texture[Foot.RIGHT]
            left_tex = self.supporting_foot_texture[Foot.LEFT]
        else:
            left_tex = self.free_foot_texture[Foot.LEFT]
            right_tex = self.free_foot_texture[Foot.RIGHT]

        arcade.draw_texture_rectangle(self.position[Foot.LEFT].x, self.position[Foot.LEFT].y,
                                      left_tex.width, left_tex.height, left_tex, self.position[Foot.LEFT].angle)
        arcade.draw_texture_rectangle(self.position[Foot.RIGHT].x, self.position[Foot.RIGHT].y,
                                      right_tex.width, right_tex.height, right_tex, self.position[Foot.RIGHT].angle)
