import Step
import Dance
import Song
import arcade
import pyglet

class Foxtrot(Dance.Dance):

    def __init__(self):
        super().__init__()
        self.name = arcade.create_text("F: Foxtrot", arcade.color.BLACK, 14)

    def basic(self):
        f = Step.Figure("1: Basic")
        self.forward_pixels = 210
        self.side_pixels = 80

        # Step 1 - Forward Slow
        f.add_leader_step(Step.Forward(Step.Foot.LEFT, self.forward_pixels, self.seconds_per_beat * 2))
        f.add_follower_step(Step.Backward(Step.Foot.RIGHT, self.forward_pixels, self.seconds_per_beat * 2))

        # Step 2 - Forward Slow
        f.add_leader_step(Step.Forward(Step.Foot.RIGHT, self.forward_pixels, self.seconds_per_beat * 2))
        f.add_follower_step(Step.Backward(Step.Foot.LEFT, self.forward_pixels, self.seconds_per_beat * 2))

        # Step 3 - Side Quick
        f.add_leader_step(Step.Side(Step.Foot.LEFT, -self.side_pixels, self.seconds_per_beat))
        f.add_follower_step(Step.Side(Step.Foot.RIGHT, self.side_pixels, self.seconds_per_beat))

        # Step 4 - Close the feet
        f.add_leader_step(Step.Close(Step.Foot.RIGHT, self.seconds_per_beat))
        f.add_follower_step(Step.Close(Step.Foot.LEFT, self.seconds_per_beat))

        return f

    def load_figures(self):
        self.figure_list.append(self.basic())

    def load_songs(self):
        self.song_list.append(Song.Song(1, "Music/Foxtrot/The Pink Panther Theme.mp3", 116))
