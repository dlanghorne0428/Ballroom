import Step
from Figure import Figure
import Dance
import Song
import pyglet
import arcade

class Rumba(Dance.Dance):

    def __init__(self):
        super().__init__()
        self.name = arcade.create_text("R: Rumba", arcade.color.BLACK, 24)
        self.beats_per_minute = 120      # BPM is provided by the selected song
        self.seconds_per_beat = 60 / self.beats_per_minute

    class Rumba_Box(Figure):

        def __init__(self, timing):
            super().__init__("Rumba Box")

            self.customization_needed = True
            self.customization_count = 0
            self.define_menu_item("a. Front Half of Box")
            self.define_menu_item("b. Back Half of Box")
            self.define_menu_item("c. Full Box")
            self.beat_time = timing

            self.front_half = None  # first customization determines what parts of box to do
            self.back_half = None

        def customize(self, index):
            self.customization_count += 1
            if self.customization_count == 1:
                self.front_step_pixels = 120
                self.side_step_pixels = 80
                self.front_half = False
                self.back_half = False
                if index == 0 or index == 2:
                    self.front_half = True
                if index == 1 or index == 2:
                    self.back_half = True
                self.clear_menu_items()
                self.define_menu_item("a: No Turn")
                self.define_menu_item("b: 1/8 Turn")
                self.define_menu_item("c: 1/4 Turn")
            else:
                if index == 0:   # no_turn
                    angle_1 = 0
                    angle_2 = 0
                elif index == 1:
                    angle_1 = 10
                    angle_2 = 12.5
                else:
                    angle_1 = 20
                    angle_2 = 25

                if self.front_half:
                    # Rumba - Step 1 Slow
                    self.add_leader_step(Step.Forward(Step.Foot.LEFT, self.front_step_pixels, self.beat_time * 2, pre_step_pivot=angle_1))
                    self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time * 2))

                    # Rumba - Step 2 Quick
                    self.add_leader_step(Step.Side(Step.Foot.RIGHT, self.side_step_pixels, self.beat_time, pre_step_pivot=angle_2))
                    self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time))

                    # Rumba - Step 3 Quick
                    self.add_leader_step(Step.Close(Step.Foot.LEFT, self.beat_time))
                    self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time))

                if self.back_half:
                    # Rumba - Step 4 Slow
                    self.add_leader_step(Step.Backward(Step.Foot.RIGHT, self.front_step_pixels, self.beat_time * 2, pre_step_pivot=angle_2))
                    self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time * 2))

                    # Rumba - Step 5 Quick
                    self.add_leader_step(Step.Side(Step.Foot.LEFT, self.side_step_pixels, self.beat_time, pre_step_pivot=angle_1))
                    self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time))

                    # Rumba - Step 6 Quick
                    self.add_leader_step(Step.Close(Step.Foot.RIGHT, self.beat_time))
                    self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time))

                self.customization_needed = False

    def alt_basic(self):

        f = Figure("Alternative Basic")
        pixels_per_front_step = 60
        pixels_per_side_step = 80

        # Rumba - Step 1 Slow : left foot side
        f.add_leader_step(Step.Side(Step.Foot.LEFT, pixels_per_side_step, self.seconds_per_beat * 2))
        f.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.seconds_per_beat * 2))

        # Rumba - Step 2 Quick: rock back on right
        f.add_leader_step(Step.Backward(Step.Foot.RIGHT, pixels_per_front_step, self.seconds_per_beat))
        f.add_follower_step(Step.Follow(Step.Foot.LEFT, self.seconds_per_beat))

        # Rumba - Step 3 Quick : replace weight
        f.add_leader_step(Step.Step(Step.Foot.LEFT, self.seconds_per_beat))
        f.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.seconds_per_beat))

        # Rumba - Step 4 Slow : right foot side
        f.add_leader_step(Step.Side(Step.Foot.RIGHT, pixels_per_side_step, self.seconds_per_beat * 2))
        f.add_follower_step(Step.Follow(Step.Foot.LEFT, self.seconds_per_beat * 2))

        # Rumba - Step 5 Quick: rock forward on left
        f.add_leader_step(Step.Forward(Step.Foot.LEFT, pixels_per_front_step, self.seconds_per_beat))
        f.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.seconds_per_beat))

        # Rumba - Step 6 Quick : replace weight
        f.add_leader_step(Step.Step(Step.Foot.RIGHT, self.seconds_per_beat))
        f.add_follower_step(Step.Follow(Step.Foot.LEFT, self.seconds_per_beat))

        return f

    class Cuban_Walk(Figure):
        def __init__(self, timing):
            super().__init__("Cuban Walk")

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
            self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time * 2))

            # Rumba - Step 2 Quick: right foot forward
            self.add_leader_step(Step.Forward(Step.Foot.RIGHT, pixels_per_front_step, self.beat_time))
            self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time))

            # Rumba - Step 3 Quick : left foot forward
            self.add_leader_step(Step.Forward(Step.Foot.LEFT, pixels_per_front_step, self.beat_time))
            self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time))

            # Rumba - Step 4 Slow : right foot forward
            self.add_leader_step(Step.Forward(Step.Foot.RIGHT, pixels_per_front_step, self.beat_time * 2))
            self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time * 2))

            # Rumba - Step 5 Quick: left foot forward
            self.add_leader_step(Step.Forward(Step.Foot.LEFT, pixels_per_front_step, self.beat_time))
            self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time))

            # Rumba - Step 6 Quick : right foot forward
            self.add_leader_step(Step.Forward(Step.Foot.RIGHT, pixels_per_front_step, self.beat_time))
            self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time))

            # done with customization
            self.customization_needed = False



    def load_figure_names(self):
        self.figure_names.append(arcade.create_text("1: Rumba Box", arcade.color.BLACK, 14))
        self.figure_names.append(arcade.create_text("2: Alternative Basic", arcade.color.BLACK, 14))
        self.figure_names.append(arcade.create_text("3: Cuban Walk", arcade.color.BLACK, 14))

    def select_figure(self, index):
        if index == 0:
            self.current_figure = self.Rumba_Box(self.seconds_per_beat)
        elif index == 1:
            self.current_figure = self.alt_basic()
        else:
            self.current_figure = self.Cuban_Walk(self.seconds_per_beat)
        if not self.current_figure.customization_needed:
            self.current_routine.append(self.current_figure)
        return self.current_figure

    def load_songs(self):
        self.song_list.append(Song.Song(1, "Music/Rumba/She Will Be Loved.mp3", 102, 5.0))
