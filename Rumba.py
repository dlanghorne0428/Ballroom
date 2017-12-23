import Step
from Figure import Figure
import Dance
import Song
import pyglet
import arcade

class Rumba(Dance.Dance):

    def __init__(self):
        super().__init__()
        self.name = arcade.create_text("R: Rumba", arcade.color.BLACK, 14)

    def rumba_box(self):

        f = Figure("1: Rumba Box")
        pixels_per_front_step = 120
        pixels_per_side_step = 80

        # Rumba - Step 1 Slow
        f.add_leader_step(Step.Forward(Step.Foot.LEFT, pixels_per_front_step * 0.5, self.seconds_per_beat * 2, pre_step_turn=20, rotation=25))
        f.add_follower_step(Step.Backward(Step.Foot.RIGHT, pixels_per_front_step * 1.5, self.seconds_per_beat * 2, pre_step_turn=70, rotation=-25))

        # Rumba - Step 2 Quick
        f.add_leader_step(Step.Side(Step.Foot.RIGHT, pixels_per_side_step, self.seconds_per_beat))
        f.add_follower_step(Step.Side(Step.Foot.LEFT, -pixels_per_side_step, self.seconds_per_beat))

        # Rumba - Step 3 Quick
        f.add_leader_step(Step.Close(Step.Foot.LEFT, self.seconds_per_beat))
        f.add_follower_step(Step.Close(Step.Foot.RIGHT, self.seconds_per_beat))

        # Rumba - Step 4 Slow
        f.add_leader_step(Step.Backward(Step.Foot.RIGHT, pixels_per_front_step, self.seconds_per_beat * 2))
        f.add_follower_step(Step.Forward(Step.Foot.LEFT, pixels_per_front_step, self.seconds_per_beat * 2))

        # Rumba - Step 5 Quick
        f.add_leader_step(Step.Side(Step.Foot.LEFT, -pixels_per_side_step, self.seconds_per_beat))
        f.add_follower_step(Step.Side(Step.Foot.RIGHT, pixels_per_side_step, self.seconds_per_beat))

        # Rumba - Step 6 Quick
        f.add_leader_step(Step.Close(Step.Foot.RIGHT, self.seconds_per_beat))
        f.add_follower_step(Step.Close(Step.Foot.LEFT, self.seconds_per_beat))

        return f

    def alt_basic(self):

        f = Figure("2: Alternative Basic")
        pixels_per_front_step = 60
        pixels_per_side_step = 80

        # Rumba - Step 1 Slow : left foot side
        f.add_leader_step(Step.Side(Step.Foot.LEFT, -pixels_per_side_step, self.seconds_per_beat * 2))
        f.add_follower_step(Step.Side(Step.Foot.RIGHT, pixels_per_side_step, self.seconds_per_beat * 2))

        # Rumba - Step 2 Quick: rock back on right
        f.add_leader_step(Step.Backward(Step.Foot.RIGHT, pixels_per_front_step, self.seconds_per_beat))
        f.add_follower_step(Step.Forward(Step.Foot.LEFT, pixels_per_front_step, self.seconds_per_beat))

        # Rumba - Step 3 Quick : replace weight
        f.add_leader_step(Step.Step(Step.Foot.LEFT, self.seconds_per_beat))
        f.add_follower_step(Step.Step(Step.Foot.RIGHT, self.seconds_per_beat))

        # Rumba - Step 4 Slow : right foot side
        f.add_leader_step(Step.Side(Step.Foot.RIGHT, pixels_per_side_step, self.seconds_per_beat * 2))
        f.add_follower_step(Step.Side(Step.Foot.LEFT, -pixels_per_side_step, self.seconds_per_beat * 2))

        # Rumba - Step 5 Quick: rock forward on left
        f.add_leader_step(Step.Forward(Step.Foot.LEFT, pixels_per_front_step, self.seconds_per_beat))
        f.add_follower_step(Step.Backward(Step.Foot.RIGHT, pixels_per_front_step, self.seconds_per_beat))

        # Rumba - Step 6 Quick : replace weight
        f.add_leader_step(Step.Step(Step.Foot.RIGHT, self.seconds_per_beat))
        f.add_follower_step(Step.Step(Step.Foot.LEFT, self.seconds_per_beat))

        return f

    class Cuban_Walk(Figure):
        def __init__(self, timing):
            super().__init__("3: Cuban Walk")

            self.customization_needed = True
            self.define_menu_item("a. Forward")
            self.define_menu_item("b. Backward")
            self.beat_time = timing

        def customize(self, index):
            if index == 0:
                pixels_per_front_step = 60  # leader moves forward
            else:
                pixels_per_front_step = -60 # leader moves back

            # Rumba - Step 1 Slow : left foot forward
            self.add_leader_step(Step.Forward(Step.Foot.LEFT, pixels_per_front_step, self.beat_time * 2))
            self.add_follower_step(Step.Backward(Step.Foot.RIGHT, pixels_per_front_step, self.beat_time * 2))

            # Rumba - Step 2 Quick: right foot forward
            self.add_leader_step(Step.Forward(Step.Foot.RIGHT, pixels_per_front_step, self.beat_time))
            self.add_follower_step(Step.Backward(Step.Foot.LEFT, pixels_per_front_step, self.beat_time))

            # Rumba - Step 3 Quick : left foot forward
            self.add_leader_step(Step.Forward(Step.Foot.LEFT, pixels_per_front_step, self.beat_time))
            self.add_follower_step(Step.Backward(Step.Foot.RIGHT, pixels_per_front_step, self.beat_time))

            # Rumba - Step 4 Slow : right foot forward
            self.add_leader_step(Step.Forward(Step.Foot.RIGHT, pixels_per_front_step, self.beat_time * 2))
            self.add_follower_step(Step.Backward(Step.Foot.LEFT, pixels_per_front_step, self.beat_time * 2))

            # Rumba - Step 5 Quick: left foot forward
            self.add_leader_step(Step.Forward(Step.Foot.LEFT, pixels_per_front_step, self.beat_time))
            self.add_follower_step(Step.Backward(Step.Foot.RIGHT, pixels_per_front_step, self.beat_time))

            # Rumba - Step 6 Quick : right foot forward
            self.add_leader_step(Step.Forward(Step.Foot.RIGHT, pixels_per_front_step, self.beat_time))
            self.add_follower_step(Step.Backward(Step.Foot.LEFT, pixels_per_front_step, self.beat_time))


    def load_figures(self):
        self.figure_list.append(self.rumba_box())
        self.figure_list.append(self.alt_basic())
        self.figure_list.append(self.Cuban_Walk(self.seconds_per_beat))

    def load_songs(self):
        self.song_list.append(Song.Song(1, "Music/Rumba/She Will Be Loved.mp3", 102, 5.0))
