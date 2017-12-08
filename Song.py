import arcade
import pyglet

class Song():

    def __init__(self, filename, bpm, seek = 0):
        self.filename = filename
        self.bpm = bpm
        self.seek = seek
        # strip this down to the base filename
        self.menu_text = arcade.create_text(self.filename, arcade.color.BLACK, 14)
        self.audio_stream = None
        self.player = None

    def draw_menu_entry(self, x, y):
        arcade.render_text(self.menu_text, x, y)

    def load(self):
        self.audio_stream = pyglet.media.load(self.filename)

    def play(self):
        from pyglet.media.player import Player
        if self.player is None:
            self.player = pyglet.media.Player()
        if not self.player.playing:
            self.player.queue(self.audio_stream)
            self.player.seek(self.seek)
            self.player.play()
