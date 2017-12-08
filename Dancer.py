import arcade
import math

import Step
import Position



class Dancer():
    def __init__(self):
        # the position values are coordinate values for the center of each foot
        # the angle values are the angle of each foot
        self.left_position = Position.Position()
        self.right_position = Position.Position()

        # the x and y update values are in pixels per second
        # the angle update values are in degrees per second
        self.left_update = Position.Position()
        self.right_update = Position.Position()

        self.free_foot_texture = [None, None]
        self.supporting_foot_texture = [None, None]
        self.free_foot = None

        self.routine = []
        self.current_time = 0
        self.current_step = -1  # dance hasn't started yet

    def load_free_foot_texture(self, foot, filename):
        index = int(foot)
        self.free_foot_texture[foot] = arcade.load_texture(filename)

    def load_supporting_foot_texture(self, foot, filename):
        index = int(foot)
        self.supporting_foot_texture[index] = arcade.load_texture(filename)

    def set_left_position (self, x, y, angle):
        self.left_position.set_position(x, y, angle)

    def set_right_position (self, x, y, angle):
        self.right_position.set_position(x, y, angle)

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
            self.left_update = step_data.get_update_vector(Step.Foot.LEFT, self.left_position, self.right_position)
            self.right_update = step_data.get_update_vector(Step.Foot.RIGHT, self.left_position, self.right_position)

        else:
            self.left_update = Position.NO_MOVEMENT
            self.right_update = Position.NO_MOVEMENT
            self.current_step = -1   # start over, should raise an event here


    def update(self, delta_time):
        if self.current_step > -1:
            self.current_time += delta_time
            if self.current_time < self.time_at_step_end:
                self.left_position.x += self.left_update.x * delta_time * math.sin(math.radians(self.left_position.angle+90))
                self.left_position.y += self.left_update.y * delta_time * math.cos(math.radians(self.left_position.angle))
                self.left_position.angle += self.left_update.angle * delta_time
                self.right_position.x += self.right_update.x * delta_time * math.sin(math.radians(self.right_position.angle+90))
                self.right_position.y += self.right_update.y * delta_time * math.cos(math.radians(self.right_position.angle))
                self.right_position.angle += self.right_update.angle * delta_time
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

        arcade.draw_texture_rectangle(self.left_position.x, self.left_position.y,
                                      left_tex.width, left_tex.height, left_tex, self.left_position.angle)
        arcade.draw_texture_rectangle(self.right_position.x, self.right_position.y,
                                      right_tex.width, right_tex.height, right_tex, self.right_position.angle)
