import arcade
import pyglet
from Dancer import Dancer
from Step import Foot
import Song

class Dance():

    def __init__(self):

        self.leader = Dancer()
        self.follower = Dancer(self.leader)

        self.figure_names = []           # list of figures available for a given dance
        self.song_list = []             # list of songs available for a given dance
        self.name = None                # the name of a given dance
        self.current_figure = None      # the current figure selected
        self.current_song = None        # the current song selected
        self.current_routine = []       # a routine is a list of figures. Start with an empty routine.

        self.beats_per_minute = 120     # BPM is provided by the selected song
        self.seconds_per_beat = 60 / self.beats_per_minute

    def customize_current_figure(self, index):
        self.current_figure.customize(index)
        if not self.current_figure.customization_needed:
            self.current_routine.append(self.current_figure)

    def draw_name(self, x, y):
        if self.name is None:
            pass
        else:
            arcade.render_text(self.name, x, y)

    def initialize_dancers(self):
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
        self.leader.set_position(Foot.RIGHT,380, 120, 0)
        self.follower.set_position(Foot.LEFT, 420, 280, 180)
        self.follower.set_position(Foot.RIGHT, 340, 280, 180)

    def prepare_dancers(self):
        # this gives the dancers their routine
        # perhaps the dancers should only know their next step?
        for fig in self.current_routine:
            for lead in fig.leader_steps:
                self.leader.add_step(lead)
            for follow in fig.follower_steps:
                self.follower.add_step(follow)

    def draw_dancers(self):
        self.leader.draw()
        self.follower.draw()

    def start_dance(self):
        self.leader.start_next_step()
        self.follower.start_next_step()

    def update_dancers(self, delta_time):
        self.leader.update(delta_time)
        self.follower.update(delta_time)

    def select_song(self, index):
        self.current_song = self.song_list[index]
        self.beats_per_minute = self.current_song.bpm
        self.seconds_per_beat = 60 / self.beats_per_minute
        self.current_song.load()

    def play_song(self):
        if self.current_song is not None:
            self.current_song.play()

    def pause_song(self):
        if self.current_song is not None:
            self.current_song.pause()
