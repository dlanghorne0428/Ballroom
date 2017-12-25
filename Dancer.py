import arcade
import math

import Step
import Position



class Dancer():
    def __init__(self, leader=None):
        # the current position of the dancer's feet
        self.position = [Position.Position(), Position.Position()]

        # the update vector of the dancer's feet. in pixels per second and degrees per second
        self.delta_pos = [Position.Position(), Position.Position()]

        # the texture images to draw for the dancer's feet.
        self.free_foot_texture = [None, None]
        self.supporting_foot_texture = [None, None]
        self.free_foot = None
        
        # a reference to the leader. If this dancer is the leader, the variable is set to None
        self.lead_dancer = leader

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
        
    # modify the angle of the given foot before the next step
    def pivot(self, foot, rotation):
        self.position[foot].angle += rotation

    def update(self, delta_time):
        for foot in range(Step.Foot.BOTH):
            self.position[foot].x += self.delta_pos[foot].x * delta_time
            self.position[foot].y += self.delta_pos[foot].y * delta_time
            self.position[foot].angle += self.delta_pos[foot].angle * delta_time

    def draw(self):
        if self.free_foot == Step.Foot.LEFT:
            left_tex = self.free_foot_texture[Step.Foot.LEFT]
            right_tex = self.supporting_foot_texture[Step.Foot.RIGHT]
        elif self.free_foot == Step.Foot.RIGHT:
            right_tex = self.free_foot_texture[Step.Foot.RIGHT]
            left_tex = self.supporting_foot_texture[Step.Foot.LEFT]
        else:
            left_tex = self.free_foot_texture[Step.Foot.LEFT]
            right_tex = self.free_foot_texture[Step.Foot.RIGHT]

        arcade.draw_texture_rectangle(self.position[Step.Foot.LEFT].x, self.position[Step.Foot.LEFT].y,
                                      left_tex.width, left_tex.height, left_tex, self.position[Step.Foot.LEFT].angle)
        arcade.draw_texture_rectangle(self.position[Step.Foot.RIGHT].x, self.position[Step.Foot.RIGHT].y,
                                      right_tex.width, right_tex.height, right_tex, self.position[Step.Foot.RIGHT].angle)
