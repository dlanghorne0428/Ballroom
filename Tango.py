import Step
import Dance
import arcade
import pyglet

class Tango(Dance.Dance):

    def __init__(self):
        super().__init__()
        self.beats_per_minute = 120   # BPM should come from song
        self.seconds_per_beat = 60 / self.beats_per_minute
        self.name = arcade.create_text("T: Tango", arcade.color.DIM_GRAY, 14)
