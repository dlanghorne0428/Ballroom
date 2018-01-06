""" The Song module defines a class to wrap a Pyglet Media player"""
import arcade
import pyglet

class Song():
    """
    The Song class wraps the Pyglet media player (load, play, pause)
    It also builds a menu entry from the filename.
    It holds the beats per minute of the song, which must be passed in.
    It does not try to analyze the song to determine the BPM, although that would be cool.
    You can optionally seek a number of seconds into the song before the initial playback
    """
    def __init__(self, index, filename, bpm, seek = 0):
        """ Constructor. The index is a number used in creating the menu entry."""
        self.filename = filename
        self.bpm = bpm
        self.seek = seek
        self.menu_entry = self.build_menu_entry(index, self.filename)
        self.menu_text = arcade.create_text(self.menu_entry, arcade.color.BLACK, 14)
        self.audio_stream = None
        self.player = None

    def build_menu_entry(self, index, filename):
        """ Create a menu entry given an index number and a full pathname."""
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

        entry = str(index) + ". " + filename
        return entry


    def draw_menu_entry(self, x, y):
        """render the menu entry at the specified (x, y) position"""
        arcade.render_text(self.menu_text, x, y)

    def load(self):
        """ create a pyglet media player for this file """
        self.audio_stream = pyglet.media.load(self.filename)

    def play(self):
        """ seek into the file and start playing the track"""
        from pyglet.media.player import Player
        if self.player is None:
            self.player = pyglet.media.Player()
        if not self.player.playing:
            self.player.queue(self.audio_stream)
            self.player.seek(self.seek)
            self.player.play()

    def pause(self):
        """ pause the track. there is no stop. """
        self.player.pause()
