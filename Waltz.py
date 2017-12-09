import Step

import Dance
import Song
import arcade

class Waltz(Dance.Dance):

    def __init__(self):
        super().__init__()
        self.name = arcade.create_text("W: Waltz", arcade.color.BLACK, 14)
        Step.Step:set_spread(80)

    def box_step(self):
        f = Step.Figure("1: Box Step")
        self.forward_pixels = 160
        self.side_pixels = 120

        # Slow Waltz - Step 1
        f.add_leader_step(Step.Forward(Step.Foot.LEFT, self.forward_pixels, self.seconds_per_beat))
        f.add_follower_step(Step.Backward(Step.Foot.RIGHT, self.forward_pixels, self.seconds_per_beat))

        # Slow Waltz - Step 2
        f.add_leader_step(Step.Side(Step.Foot.RIGHT, self.side_pixels, self.seconds_per_beat))
        f.add_follower_step(Step.Side(Step.Foot.LEFT, -self.side_pixels, self.seconds_per_beat))

        # Slow Waltz - Step 3
        f.add_leader_step(Step.Close(Step.Foot.LEFT, self.seconds_per_beat))
        f.add_follower_step(Step.Close(Step.Foot.RIGHT, self.seconds_per_beat))

        # Slow Waltz - Step 4
        f.add_leader_step(Step.Backward(Step.Foot.RIGHT, self.forward_pixels, self.seconds_per_beat))
        f.add_follower_step(Step.Forward(Step.Foot.LEFT, self.forward_pixels, self.seconds_per_beat))

        # Slow Waltz - Step 5
        f.add_leader_step(Step.Side(Step.Foot.LEFT, -self.side_pixels, self.seconds_per_beat))
        f.add_follower_step(Step.Side(Step.Foot.RIGHT, self.side_pixels, self.seconds_per_beat))

        # Slow Waltz - Step 6
        f.add_leader_step(Step.Close(Step.Foot.RIGHT, self.seconds_per_beat))
        f.add_follower_step(Step.Close(Step.Foot.LEFT, self.seconds_per_beat))

        return f

    def load_figures(self):
        self.figure_list.append(self.box_step())

    def load_songs(self):
        self.song_list.append(Song.Song(1, "Music/Waltz/Come Away With Me.mp3", 80, 17.25))
        self.song_list.append(Song.Song(2, "Music/Waltz/Dark Waltz.mp3", 87, 17))
