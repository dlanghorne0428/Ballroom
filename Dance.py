import arcade
import pyglet
import Song

class Dance():

    def __init__(self):

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
