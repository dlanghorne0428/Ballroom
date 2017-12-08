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
        self.player = None
        self.beats_per_minute = 120   # BPM should come from song
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
        self.current_audio_stream = pyglet.media.load(self.current_song.filename)

    def play_song(self):
        from pyglet.media.player import Player
        if self.player is None:
            self.player = pyglet.media.Player()
        if not self.player.playing:
            self.player.queue(self.current_audio_stream)
            self.player.play()
        # arcade.sound.play_sound(self.current_song)
