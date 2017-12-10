import Step
import Dance
import Song
import pyglet
import arcade

class Rumba(Dance.Dance):

    def __init__(self):
        super().__init__()
        self.name = arcade.create_text("R: Rumba", arcade.color.BLACK, 14)

    def rumba_box(self):

        f = Step.Figure("1: Rumba Box")
        pixels_per_front_step = 120
        pixels_per_side_step = 80

        # Rumba - Step 1 Slow
        f.add_leader_step(Step.Forward(Step.Foot.LEFT, pixels_per_front_step, self.seconds_per_beat * 2))
        f.add_follower_step(Step.Backward(Step.Foot.RIGHT, pixels_per_front_step, self.seconds_per_beat * 2))

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

        f = Step.Figure("2: Alternative Basic")
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

    def cuban_walk_forward(self):

        f = Step.Figure("3: Cuban Walk Forward")
        pixels_per_front_step = 60

        # Rumba - Step 1 Slow : left foot forward
        f.add_leader_step(Step.Forward(Step.Foot.LEFT, pixels_per_front_step, self.seconds_per_beat * 2))
        f.add_follower_step(Step.Backward(Step.Foot.RIGHT, pixels_per_front_step, self.seconds_per_beat * 2))

        # Rumba - Step 2 Quick: right foot forward
        f.add_leader_step(Step.Forward(Step.Foot.RIGHT, pixels_per_front_step, self.seconds_per_beat))
        f.add_follower_step(Step.Backward(Step.Foot.LEFT, pixels_per_front_step, self.seconds_per_beat))

        # Rumba - Step 3 Quick : left foot forward
        f.add_leader_step(Step.Forward(Step.Foot.LEFT, pixels_per_front_step, self.seconds_per_beat))
        f.add_follower_step(Step.Backward(Step.Foot.RIGHT, pixels_per_front_step, self.seconds_per_beat))

        # Rumba - Step 4 Slow : right foot forward
        f.add_leader_step(Step.Forward(Step.Foot.RIGHT, pixels_per_front_step, self.seconds_per_beat * 2))
        f.add_follower_step(Step.Backward(Step.Foot.LEFT, pixels_per_front_step, self.seconds_per_beat * 2))

        # Rumba - Step 5 Quick: left foot forward
        f.add_leader_step(Step.Forward(Step.Foot.LEFT, pixels_per_front_step, self.seconds_per_beat))
        f.add_follower_step(Step.Backward(Step.Foot.RIGHT, pixels_per_front_step, self.seconds_per_beat))

        # Rumba - Step 6 Quick : right foot forward
        f.add_leader_step(Step.Forward(Step.Foot.RIGHT, pixels_per_front_step, self.seconds_per_beat))
        f.add_follower_step(Step.Backward(Step.Foot.LEFT, pixels_per_front_step, self.seconds_per_beat))

        return f

    def load_figures(self):
        self.figure_list.append(self.rumba_box())
        self.figure_list.append(self.alt_basic())
        self.figure_list.append(self.cuban_walk_forward())

    def load_songs(self):
        self.song_list.append(Song.Song(1, "Music/Rumba/She Will Be Loved.mp3", 102, 5.0))
