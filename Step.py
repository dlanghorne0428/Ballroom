from enum import IntEnum
import arcade

class Foot(IntEnum):
    LEFT = 0
    RIGHT = 1
    BOTH = 2
    
class Step():
    
    def __init__(self, foot, x_dist, y_dist, rotation, duration, x_dist_r = 0, y_dist_r = 0, rot_2 = 0):
        self.duration = duration
        self.foot = foot
        if foot == Foot.LEFT:
            self.x_distance_left = x_dist
            self.y_distance_left = y_dist
            self.rotation_angle_left = rotation
            self.x_distance_right = 0
            self.y_distance_right = 0
            self.rotation_angle_right = 0
        elif foot == Foot.RIGHT:
            self.x_distance_right = x_dist
            self.y_distance_right = y_dist
            self.rotation_angle_right = rotation
            self.x_distance_left = 0
            self.y_distance_left = 0
            self.rotation_angle_left = 0            
        else:
            self.x_distance_left = x_dist
            self.y_distance_left = y_dist
            self.rotation_angle_left = rotation
            self.x_distance_right = x_dist_r
            self.y_distance_right = y_dist_r
            self.rotation_angle_right = rot_r  
            
class Figure():
    # a Figure is a list of steps for both leader and follower
    
    def __init__(self, name):
        self.leader_steps = []
        self.follower_steps = []
        self.name = arcade.create_text(name, arcade.color.BLACK, 14)
        
    def add_leader_step(self, foot, x_dist, y_dist, rotation, duration):
        s = Step(foot, x_dist, y_dist, rotation, duration)
        self.leader_steps.append(s)
        
    def add_follower_step(self, foot, x_dist, y_dist, rotation, duration):
        s = Step(foot, x_dist, y_dist, rotation, duration)
        self.follower_steps.append(s) 
        
    def draw_name(self, x, y):
        arcade.render_text(self.name, x, y)