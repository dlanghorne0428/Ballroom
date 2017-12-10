import arcade
import pyglet

def base_filename(index, filename):
    done = False
    #strip off the folder names
    while not done:
        pos = filename.find("/")
        if pos == -1:
            done = True
        else:
            filename = filename[pos+1:]

    # strip off the extension
    pos = filename.find(".")
    if pos != -1:
        filename = filename[:pos]

    filename = str(index) + ". " + filename

    return filename

class Song():

    def __init__(self, index, filename, bpm, seek = 0):
        self.filename = filename
        self.bpm = bpm
        self.seek = seek
        self.menu_entry = base_filename(index, self.filename)
        self.menu_text = arcade.create_text(self.menu_entry, arcade.color.BLACK, 14)
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

    def pause(self):
        self.player.pause()
