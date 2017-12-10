import arcade
import math

import Step
import Position



class Dancer():
    def __init__(self):
        # the current position of the dancer's feet
        self.position = [Position.Position(), Position.Position()]

        # the update vector of the dancer's feet. in pixels per second and degrees per second
        self.delta_pos = [Position.Position(), Position.Position()]

        # the texture images to draw for the dancer's feet.
        self.free_foot_texture = [None, None]
        self.supporting_foot_texture = [None, None]
        self.free_foot = None

        self.routine = []
        self.current_time = 0
        self.current_step = -1  # dance hasn't started yet

    def load_free_foot_texture(self, foot, filename):
        self.free_foot_texture[foot] = arcade.load_texture(filename)

    def load_supporting_foot_texture(self, foot, filename):
        self.supporting_foot_texture[foot] = arcade.load_texture(filename)

    def set_position (self, foot, x, y, angle):
        self.position[foot].set(x, y, angle)

    def set_free_foot(self, foot):
        self.free_foot = foot

    def add_step(self, step):
        self.routine.append(step)

    def start_next_step(self):
        self.current_step += 1
        if self.current_step < len(self.routine):
            step_data = self.routine[self.current_step]
            self.free_foot = step_data.foot
            self.time_at_step_end = self.current_time + step_data.duration
            for foot in range(Step.Foot.BOTH):
                self.delta_pos[foot] = step_data.get_update_vector(foot, self.position)

        else:
            for foot in range(Step.Foot.BOTH):
                self.delta_pos[foot] = Position.NO_MOVEMENT
            self.current_step = -1   # start over, should raise an event here


    def update(self, delta_time):
        if self.current_step > -1:
            self.current_time += delta_time
            if self.current_time < self.time_at_step_end:
                for foot in range(Step.Foot.BOTH):
                    self.position[foot].x += self.delta_pos[foot].x * delta_time
                    self.position[foot].y += self.delta_pos[foot].y * delta_time
                    # self.position[foot].x += self.delta_pos[foot].x * delta_time * math.sin(math.radians(self.position[foot].angle+90))
                    # self.position[foot].y += self.delta_pos[foot].y * delta_time * math.cos(math.radians(self.position[foot].angle))
                    self.position[foot].angle += self.delta_pos[foot].angle * delta_time
            else:
                self.start_next_step()


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
