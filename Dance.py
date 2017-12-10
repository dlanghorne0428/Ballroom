import arcade
import pyglet
import Song

class Dance():

    def __init__(self):
        self.figure_list = []
        self.song_list = []
        self.name = None
        self.current_figure = None
        self.current_song = None
        self.beats_per_minute = 120   # BPM is provided by the selected song
        self.seconds_per_beat = 60 / self.beats_per_minute

    def get_figure(self, index):
        self.current_figure = self.figure_list[index]
        return self.current_figure

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
        self.current_song.play()
