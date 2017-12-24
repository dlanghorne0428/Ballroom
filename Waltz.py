import Step
from Figure import Figure
import Dance
import Song
import arcade

class Waltz(Dance.Dance):

    def __init__(self):
        super().__init__()
        self.name = arcade.create_text("W: Waltz", arcade.color.BLACK, 14)
        Step.Step:set_spread(80)

    def left_box_turn(self):
        f = Figure("Left Box Turn")
        self.forward_pixels = 160
        self.side_pixels = 120

        # Slow Waltz - Step 1 quarter turn for now
        f.add_leader_step(Step.Forward(Step.Foot.LEFT, self.forward_pixels, self.seconds_per_beat, 90))
        f.add_follower_step(Step.Backward(Step.Foot.RIGHT, self.forward_pixels, self.seconds_per_beat,90 ))

        # # Slow Waltz - Step 2
        f.add_leader_step(Step.Side(Step.Foot.RIGHT, self.side_pixels, self.seconds_per_beat))
        f.add_follower_step(Step.Side(Step.Foot.LEFT, -self.side_pixels, self.seconds_per_beat))
        #
        # # Slow Waltz - Step 3
        # f.add_leader_step(Step.Close(Step.Foot.LEFT, self.seconds_per_beat))
        # f.add_follower_step(Step.Close(Step.Foot.RIGHT, self.seconds_per_beat))
        #
        # # Slow Waltz - Step 4
        # f.add_leader_step(Step.Backward(Step.Foot.RIGHT, self.forward_pixels, self.seconds_per_beat))
        # f.add_follower_step(Step.Forward(Step.Foot.LEFT, self.forward_pixels, self.seconds_per_beat))
        #
        # # Slow Waltz - Step 5
        # f.add_leader_step(Step.Side(Step.Foot.LEFT, -self.side_pixels, self.seconds_per_beat))
        # f.add_follower_step(Step.Side(Step.Foot.RIGHT, self.side_pixels, self.seconds_per_beat))
        #
        # # Slow Waltz - Step 6
        # f.add_leader_step(Step.Close(Step.Foot.RIGHT, self.seconds_per_beat))
        # f.add_follower_step(Step.Close(Step.Foot.LEFT, self.seconds_per_beat))

        return f

    def right_box_turn(self):
        f = Figure("Right Box Turn")
        self.forward_pixels = 160
        self.side_pixels = 120

        # Slow Waltz - Step 1
        f.add_leader_step(Step.Forward(Step.Foot.RIGHT, self.forward_pixels, self.seconds_per_beat))
        f.add_follower_step(Step.Backward(Step.Foot.LEFT, self.forward_pixels, self.seconds_per_beat))

        # Slow Waltz - Step 2
        f.add_leader_step(Step.Side(Step.Foot.LEFT, -self.side_pixels, self.seconds_per_beat))
        f.add_follower_step(Step.Side(Step.Foot.RIGHT, self.side_pixels, self.seconds_per_beat))

        # Slow Waltz - Step 3
        f.add_leader_step(Step.Close(Step.Foot.RIGHT, self.seconds_per_beat))
        f.add_follower_step(Step.Close(Step.Foot.LEFT, self.seconds_per_beat))

        # Slow Waltz - Step 4
        f.add_leader_step(Step.Backward(Step.Foot.LEFT, self.forward_pixels, self.seconds_per_beat))
        f.add_follower_step(Step.Forward(Step.Foot.RIGHT, self.forward_pixels, self.seconds_per_beat))

        # Slow Waltz - Step 5
        f.add_leader_step(Step.Side(Step.Foot.RIGHT, self.side_pixels, self.seconds_per_beat))
        f.add_follower_step(Step.Side(Step.Foot.LEFT, -self.side_pixels, self.seconds_per_beat))

        # Slow Waltz - Step 6
        f.add_leader_step(Step.Close(Step.Foot.LEFT, self.seconds_per_beat))
        f.add_follower_step(Step.Close(Step.Foot.RIGHT, self.seconds_per_beat))

        return f

    def change_step(self):
        f = Figure("Change Step")
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

        return f

    def load_figure_names(self):
        self.figure_names.append(arcade.create_text("1: Left Box Turn", arcade.color.BLACK, 14))
        self.figure_names.append(arcade.create_text("2. Right Box Turn", arcade.color.BLACK, 14))
        self.figure_names.append(arcade.create_text("3: Change Step", arcade.color.BLACK, 14))

    def select_figure(self, index):
        if index == 0:
            self.current_figure = self.left_box_turn()
        elif index == 1:
            self.current_figure = self.right_box_turn()
        else:
            self.current_figure = self.change_step()
        if not self.current_figure.customization_needed:
            self.current_routine.append(self.current_figure)
        return self.current_figure

    def load_songs(self):
        self.song_list.append(Song.Song(1, "Music/Waltz/Come Away With Me.mp3", 80, 17.25))
        self.song_list.append(Song.Song(2, "Music/Waltz/Dark Waltz.mp3", 87, 17))
