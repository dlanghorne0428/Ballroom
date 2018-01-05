import Step
from Figure import Figure
import Dance
import Song
import arcade

class Waltz(Dance.Dance):

    def __init__(self):
        super().__init__()
        self.name = arcade.create_text("W: Waltz", arcade.color.BLACK, 14)
        Step.Step:set_spread(0)
        self.beats_per_minute = 84      # BPM is provided by the selected song
        self.seconds_per_beat = 60 / self.beats_per_minute

    def lf_change(fig, timing, fwd_pixels, side_pixels, piv_angle_1 = 0, piv_angle_2 = 0, rot_angle_1 = 0, rot_angle_2 = 0, leader_only=False):
        fig.add_leader_step(Step.Forward(Step.Foot.LEFT, fwd_pixels, timing, pre_step_pivot=piv_angle_1, rotation=rot_angle_1))
        fig.add_leader_step(Step.Side(Step.Foot.RIGHT, side_pixels, timing, pre_step_pivot=piv_angle_2, rotation=rot_angle_2))
        fig.add_leader_step(Step.Close(Step.Foot.LEFT, timing))

        if not leader_only:
            fig.add_follower_step(Step.Follow(Step.Foot.RIGHT, timing))
            fig.add_follower_step(Step.Follow(Step.Foot.LEFT, timing))
            fig.add_follower_step(Step.Follow(Step.Foot.RIGHT, timing))

    def rf_change(fig, timing, fwd_pixels, side_pixels, piv_angle_1 = 0, piv_angle_2 = 0, rot_angle_1 = 0, rot_angle_2 = 0, leader_only=False):
        # Step 1 - Backward Right
        fig.add_leader_step(Step.Forward(Step.Foot.RIGHT, fwd_pixels, timing, pre_step_pivot=piv_angle_1, rotation=rot_angle_1))
        fig.add_leader_step(Step.Side(Step.Foot.LEFT, -side_pixels, timing, pre_step_pivot=piv_angle_2, rotation=rot_angle_2))
        fig.add_leader_step(Step.Close(Step.Foot.RIGHT, timing))

        if not leader_only:
            fig.add_follower_step(Step.Follow(Step.Foot.LEFT, timing))
            fig.add_follower_step(Step.Follow(Step.Foot.RIGHT, timing))
            fig.add_follower_step(Step.Follow(Step.Foot.LEFT, timing))


    class Left_Box_Turn(Figure):

        def __init__(self, timing):
            super().__init__("Left Box Turn")
            self.customization_needed = True
            self.beat_time = timing
            self.define_menu_item("a. No Turn")
            self.define_menu_item("b. 1/4 Turn")
            self.define_menu_item("c. 3/8 Turn")

        def customize(self, index):
            forward_pixels = 160
            side_pixels = 160
            if index == 0:
                rot_angle_1 = 0
                rot_angle_2 = 0
                pivot_angle_1 = 0
                pivot_angle_2 = 0
            elif index == 1:
                pivot_angle_1 = 10
                rot_angle_1 = 30
                rot_angle_2 = 20
                pivot_angle_2 = 30
            else:
                pivot_angle_1 = 10
                rot_angle_1 = 45
                pivot_angle_2 = 60
                rot_angle_2 = 30

            Waltz.lf_change(self, self.beat_time, forward_pixels, side_pixels, pivot_angle_1, pivot_angle_2, rot_angle_1, rot_angle_2)
            Waltz.rf_change(self, self.beat_time, -forward_pixels, side_pixels, pivot_angle_1, pivot_angle_2, rot_angle_1, rot_angle_2)

            self.customization_needed = False

    class Right_Box_Turn(Figure):
        def __init__(self, timing):
            super().__init__("Right Box Turn")
            self.customization_needed = True
            self.beat_time = timing
            self.define_menu_item("a. No Turn")
            self.define_menu_item("b. 1/4 Turn")
            self.define_menu_item("c. 3/8 Turn")

        def customize(self, index):
            forward_pixels = 160
            side_pixels = 160
            if index == 0:
                rot_angle_1 = 0
                rot_angle_2 = 0
                pivot_angle_1 = 0
                pivot_angle_2 = 0
            elif index == 1:
                pivot_angle_1 = -10
                rot_angle_1 = -30
                rot_angle_2 = -20
                pivot_angle_2 = -30
            else:
                pivot_angle_1 = -10
                rot_angle_1 = -45
                pivot_angle_2 = -60
                rot_angle_2 = -30

            Waltz.rf_change(self, self.beat_time, forward_pixels, side_pixels, pivot_angle_1, pivot_angle_2, rot_angle_1, rot_angle_2)
            Waltz.lf_change(self, self.beat_time, -forward_pixels, side_pixels, pivot_angle_1, pivot_angle_2, rot_angle_1, rot_angle_2)

            self.customization_needed = False

    class Change_Step(Figure):
        def __init__(self, timing):
            super().__init__("Change Step")
            self.customization_needed = True
            self.beat_time = timing
            self.define_menu_item("a. Forward L to R")
            self.define_menu_item("b. Forward R to L")
            self.define_menu_item("c. Backward L to R")
            self.define_menu_item("d. Backward R to L")

        def customize(self, index):
            forward_pixels = 160
            side_pixels = 160
            if index == 0:
                Waltz.lf_change(self, self.beat_time, forward_pixels, side_pixels)
            elif index == 1:
                Waltz.rf_change(self, self.beat_time, forward_pixels, side_pixels)
            elif index == 2:
                Waltz.lf_change(self, self.beat_time, -forward_pixels, side_pixels)
            else:
                Waltz.rf_change(self, self.beat_time, -forward_pixels, side_pixels)

            self.customization_needed = False

    class Six_Count_Underarm_Turn(Figure):
        def __init__(self, timing):
            super().__init__("Six-count Underarm Turn")
            self.customization_needed = False   # for now
            self.beat_time = timing
            forward_pixels = 160
            side_pixels = 160

            # leader steps
            Waltz.rf_change(self, self.beat_time, -forward_pixels, side_pixels, leader_only=True)
            Waltz.lf_change(self, self.beat_time, forward_pixels, side_pixels, piv_angle_1 = 10, piv_angle_2 = 30, rot_angle_1 = 30, rot_angle_2 = 20, leader_only=True)
                
            # follower steps
            self.add_follower_step(Step.Forward(Step.Foot.LEFT, forward_pixels * 0.75, self.beat_time))
            self.add_follower_step(Step.Forward(Step.Foot.RIGHT, forward_pixels, self.beat_time, pre_step_pivot=-45.0))  # 1/8 turn to right between 1 and 2
            self.add_follower_step(Step.Forward(Step.Foot.LEFT, forward_pixels, self.beat_time, pre_step_pivot=-45.0, rotation=-15.0))  # 1/8 turn to right between 2 and 3
            self.add_follower_step(Step.Forward(Step.Foot.RIGHT, forward_pixels, self.beat_time, pre_step_pivot=-45.0, rotation=-60.0))
            self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time))
            self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time))
#            self.add_follower_step(Step.Side(Step.Foot.LEFT, -side_pixels, self.beat_time, pre_step_pivot=-45.0, rotation=-45.0))
#            self.add_follower_step(Step.Close(Step.Foot.RIGHT, self.beat_time))
                                            

    def load_figure_names(self):
        self.figure_names.append(arcade.create_text("1: Left Box Turn", arcade.color.BLACK, 14))
        self.figure_names.append(arcade.create_text("2. Right Box Turn", arcade.color.BLACK, 14))
        self.figure_names.append(arcade.create_text("3: Change Step", arcade.color.BLACK, 14))
        self.figure_names.append(arcade.create_text("4: Six-count Underarm Turn", arcade.color.BLACK, 14))

    def select_figure(self, index):
        if index == 0:
            self.current_figure = self.Left_Box_Turn(self.seconds_per_beat)
        elif index == 1:
            self.current_figure = self.Right_Box_Turn(self.seconds_per_beat)
        elif index == 2:
            self.current_figure = self.Change_Step(self.seconds_per_beat)
        else:
            self.current_figure = self.Six_Count_Underarm_Turn(self.seconds_per_beat)
        if not self.current_figure.customization_needed:
            self.current_routine.append(self.current_figure)
        return self.current_figure

    def load_songs(self):
        self.song_list.append(Song.Song(1, "Music/Waltz/Come Away With Me.mp3", 80, 17.25))
        self.song_list.append(Song.Song(2, "Music/Waltz/Dark Waltz.mp3", 87, 17))
