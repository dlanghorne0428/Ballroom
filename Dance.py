""" The Dance module contains a base class for all dances """
import arcade
import pyglet
from Dancer import Dancer
from Step import Foot
import Position
import Song

class Dance():
    """
    The Dance() class is a base class for all dances (e.g. Waltz)
    It manages the dancers, the routine, the song, and time
    """

    def __init__(self):
        """ constructor """
        self.leader = Dancer()
        self.follower = Dancer(self.leader)  # the two dancers

        self.figure_names = []          # list of figures available for a given dance
        self.song_list = []             # list of songs available for a given dance
        self.name = None                # the name of a given dance
        self.current_figure = None      # the current figure selected or being danced
        self.current_song = None        # the current song selected
        self.current_routine = []       # a routine is a list of figures. Start with an empty routine.
        self.current_time = 0           # the current time since the start of dance, in seconds

        self.current_leader_step = None
        self.current_follower_step = None  # the current steps being danced
        self.in_progress = False        # is the dance in motion?

        self.figure_index = 0           # should use iterators, but using integer index variables for now
        self.step_index = 0             # would need separate iterators for leader and follower step list
                                        # this assumes that the leader and follower steps are the same duration.
                                        # breaking a turning step into multiple steps might break this assumption

        self.beats_per_minute = 120      # BPM default - overwritten by the selected dance or song
        self.seconds_per_beat = 60 / self.beats_per_minute

    def customize_current_figure(self, index):
        """
        Passes in an index to select an option.
        If this was the last customization for the figure, it is added to the routine
        """
        self.current_figure.customize(index)
        if not self.current_figure.customization_needed:
            self.current_routine.append(self.current_figure)

    def draw_name(self, x, y):
        """ draws the dance name at the specified (x,y) position """
        if self.name is None:
            pass
        else:
            arcade.render_text(self.name, x, y)

    def initialize_dancers(self):
        """ load foot textures and set default starting positions """
        self.leader.load_supporting_foot_texture(Foot.LEFT, "Images/man_left_foot.jpg")
        self.leader.load_supporting_foot_texture(Foot.RIGHT, "Images/man_right_foot.jpg")
        self.leader.load_free_foot_texture(Foot.LEFT, "Images/man_left_free_foot.jpg")
        self.leader.load_free_foot_texture(Foot.RIGHT, "Images/man_right_free_foot.jpg")
        self.leader.set_free_foot(Foot.LEFT)

        self.follower.load_supporting_foot_texture(Foot.LEFT, "Images/lady_left_foot.jpg")
        self.follower.load_supporting_foot_texture(Foot.RIGHT, "Images/lady_right_foot.jpg")
        self.follower.load_free_foot_texture(Foot.LEFT, "Images/lady_left_free_foot.jpg")
        self.follower.load_free_foot_texture(Foot.RIGHT, "Images/lady_right_free_foot.jpg")
        self.follower.set_free_foot(Foot.RIGHT)

        # eventually the user should be able to choose the start position
        self.leader.set_position(Foot.LEFT, 300, 120, 0)
        self.leader.set_position(Foot.RIGHT,375, 120, 0)
        self.follower.set_position(Foot.LEFT, 405, 260, 180)
        self.follower.set_position(Foot.RIGHT, 330, 260, 180)

    def draw_dancers(self):
        """ tell both dancers to draw themselves """
        self.leader.draw()
        self.follower.draw()

    def go_to_next_step(self):
        """ determine if there are more steps in this routine and set variables accordingly"""
        more_steps = True
        self.step_index += 1
        if self.step_index < len(self.current_figure.leader_steps):
            self.start_next_step()
        else:   # go to first step of next figure
            self.figure_index += 1
            self.step_index = 0
            if self.figure_index < len(self.current_routine):
                self.current_figure = self.current_routine[self.figure_index]
                self.start_next_step()
            else:  # no more figures, stop dancing
                more_steps = False
                self.figure_index = 0
                self.step_index = 0
                for foot in range(Foot.BOTH):
                    self.leader.delta_pos[foot] = Position.NO_MOVEMENT
                    self.follower.delta_pos[foot] = Position.NO_MOVEMENT

        return more_steps

    def start_next_step(self):
        """ begin the next step in the routine """
        self.current_leader_step = self.current_figure.leader_steps[self.step_index]
        self.leader.set_free_foot(self.current_leader_step.foot)
        self.current_follower_step = self.current_figure.follower_steps[self.step_index]
        self.follower.set_free_foot(self.current_follower_step.foot)

        self.time_at_next_step = self.current_time + self.current_leader_step.duration

        for foot in range(Foot.BOTH):
            self.leader.pivot(foot, self.current_leader_step.pre_step_pivot)
            leader_update_vector = self.current_leader_step.get_update_vector(foot, self.leader)
            self.leader.set_delta_pos(foot, leader_update_vector)
        for foot in range(Foot.BOTH):
            self.follower.pivot(foot, self.current_follower_step.pre_step_pivot)
            follower_update_vector = self.current_follower_step.get_update_vector(foot, self.follower)
            self.follower.set_delta_pos(foot, follower_update_vector)


    def start_dance(self):
        """ if a valid routine created, start dancing it """
        self.figure_index = 0
        if len(self.current_routine) > 0:
            # get first step of first figure and start it
            self.current_figure = self.current_routine[self.figure_index]
            self.step_index = 0
            self.current_leader_step = self.current_figure.leader_steps[self.step_index]
            self.current_follower_step = self.current_figure.follower_steps[self.step_index]
            self.start_next_step()
            # set time to 0 and indicate dance has started
            self.current_time = 0
            self.in_progress = True

    def update_dancers(self, delta_time):
        """ if dance in motion, update dancer positions """
        if self.in_progress:
            self.current_time += delta_time
            if self.current_time < self.time_at_next_step:
                # still in current step, update positions
                self.leader.update(delta_time)
                self.follower.update(delta_time)
            else:
                # current step finished, adjust final position and try to start next step
                self.leader.complete_current_step()
                self.follower.complete_current_step()
                self.in_progress = self.go_to_next_step()

        return self.in_progress

    def select_song(self, index):
        """ pick a song from the list, load file, and set BPM"""
        self.current_song = self.song_list[index]
        self.beats_per_minute = self.current_song.bpm
        self.seconds_per_beat = 60 / self.beats_per_minute
        self.current_song.load()

    def play_song(self):
        """ start playing the selected song """
        if self.current_song is not None:
            self.current_song.play()

    def pause_song(self):
        """ pause the selected song """
        if self.current_song is not None:
            self.current_song.pause()
