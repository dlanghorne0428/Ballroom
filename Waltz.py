import Step
import Dance
import arcade
import pyglet

class Waltz(Dance.Dance):

    def __init__(self):
        super().__init__()
        self.beats_per_minute = 87   # BPM should come from song
        self.seconds_per_beat = 60 / self.beats_per_minute
        self.name = arcade.create_text("W: Waltz", arcade.color.BLACK, 14)

    def box_step(self):
        f = Step.Figure("1: Box Step")
        self.pixels_per_front_step = 160
        self.pixels_per_side_step = 120

        # Slow Waltz - Step 1
        f.add_leader_step(Step.Foot.LEFT, 0, self.pixels_per_front_step, 0, self.seconds_per_beat)
        f.add_follower_step(Step.Foot.RIGHT, 0, -self.pixels_per_front_step, 0, self.seconds_per_beat)

        # Slow Waltz - Step 2
        f.add_leader_step(Step.Foot.RIGHT, self.pixels_per_side_step, 0, 0, self.seconds_per_beat)
        f.add_follower_step(Step.Foot.LEFT, -self.pixels_per_side_step, 0, 0, self.seconds_per_beat)

        # Slow Waltz - Step 3
        f.add_leader_step(Step.Foot.LEFT, self.pixels_per_side_step, 0, 0, self.seconds_per_beat)
        f.add_follower_step(Step.Foot.RIGHT, -self.pixels_per_side_step, 0, 0, self.seconds_per_beat)

        # Slow Waltz - Step 4
        f.add_leader_step(Step.Foot.RIGHT, 0, -self.pixels_per_front_step, 0, self.seconds_per_beat)
        f.add_follower_step(Step.Foot.LEFT, 0, self.pixels_per_front_step, 0, self.seconds_per_beat)

        # Slow Waltz - Step 5
        f.add_leader_step(Step.Foot.LEFT, -self.pixels_per_side_step, -0, 0, self.seconds_per_beat)
        f.add_follower_step(Step.Foot.RIGHT, self.pixels_per_side_step, 0, 0, self.seconds_per_beat)

        # Slow Waltz - Step 6
        f.add_leader_step(Step.Foot.RIGHT, -self.pixels_per_side_step, 0, 0, self.seconds_per_beat)
        f.add_follower_step(Step.Foot.LEFT, self.pixels_per_side_step, 0, 0, self.seconds_per_beat)

        return f

    def load_figures(self):
        self.figure_list.append(self.box_step())

    def load_songs(self):
        #self.song_list.append(arcade.sound.load_sound("Music/Dark Waltz.mp3"))
        self.song_list.append(pyglet.media.load("Music/Dark Waltz.mp3"))
