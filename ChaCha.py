import Step
import Dance
import arcade
import pyglet

class ChaCha(Dance.Dance):

    def __init__(self):
        super().__init__()
        self.beats_per_minute = 120   # BPM should come from song
        self.seconds_per_beat = 60 / self.beats_per_minute
        self.name = arcade.create_text("C: Cha Cha", arcade.color.BLACK, 14)

    def basic(self):
        f = Figure("Basic")
        self.forward_pixels = 80
        self.side_pixels = 80

        # Prep Step - Side
        f.add_leader_step(Step.Side(Step.Foot.RIGHT, self.side_pixels, self.seconds_per_beat))
        f.add_follower_step(Step.Backward(Step.Foot.LEFT, self.side_pixels, self.seconds_per_beat))

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

    def load_figure_names(self):
        self.figure_names.append(arcade.create_text("1: Basic", arcade.color.BLACK, 14))

    def select_figure(self, index):
        if index == 0:
            self.current_figure = self.basic()
        if not self.current_figure.customization_needed:
            self.current_routine.append(self.current_figure)
        return self.current_figure

    def load_songs(self):
        self.song_list.append(Song.Song(1, "Music/Foxtrot/The Pink Panther Theme.mp3", 116))
