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
                pivot_angle_1 = 30
                rot_angle_1 = 40
                rot_angle_2 = 20
                pivot_angle_2 = 0
            else:
                pivot_angle_1 = 30
                rot_angle_1 = 45
                pivot_angle_2 = 30
                rot_angle_2 = 30
    
            # Slow Waltz - Step 1 
            self.add_leader_step(Step.Forward(Step.Foot.LEFT, forward_pixels, self.beat_time, pre_step_pivot=pivot_angle_1, rotation=rot_angle_1))
            self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time))
    
            # Slow Waltz - Step 2
            self.add_leader_step(Step.Side(Step.Foot.RIGHT, side_pixels, self.beat_time, pre_step_pivot=pivot_angle_2, rotation=rot_angle_2))
            self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time))
            #
            # Slow Waltz - Step 3
            self.add_leader_step(Step.Close(Step.Foot.LEFT, self.beat_time))
            self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time))
            #
            # Slow Waltz - Step 4
            self.add_leader_step(Step.Backward(Step.Foot.RIGHT, forward_pixels, self.beat_time, pre_step_pivot=pivot_angle_1, rotation=rot_angle_1))
            self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time))
            #
            # Slow Waltz - Step 5
            self.add_leader_step(Step.Side(Step.Foot.LEFT, -side_pixels, self.beat_time, pre_step_pivot=pivot_angle_2, rotation=rot_angle_2))
            self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time))
            #
            # # Slow Waltz - Step 6
            self.add_leader_step(Step.Close(Step.Foot.RIGHT, self.beat_time))
            self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time))
    
            self.customization_needed = False

    def right_box_turn(self):
        f = Figure("Right Box Turn")
        self.forward_pixels = 160
        self.side_pixels = 120

        # Slow Waltz - Step 1
        f.add_leader_step(Step.Forward(Step.Foot.RIGHT, self.forward_pixels, self.seconds_per_beat))
        f.add_follower_step(Step.Follow(Step.Foot.LEFT, self.seconds_per_beat))

        # Slow Waltz - Step 2
        f.add_leader_step(Step.Side(Step.Foot.LEFT, -self.side_pixels, self.seconds_per_beat))
        f.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.seconds_per_beat))

        # Slow Waltz - Step 3
        f.add_leader_step(Step.Close(Step.Foot.RIGHT, self.seconds_per_beat))
        f.add_follower_step(Step.Follow(Step.Foot.LEFT, self.seconds_per_beat))

        # Slow Waltz - Step 4
        f.add_leader_step(Step.Backward(Step.Foot.LEFT, self.forward_pixels, self.seconds_per_beat))
        f.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.seconds_per_beat))

        # Slow Waltz - Step 5
        f.add_leader_step(Step.Side(Step.Foot.RIGHT, self.side_pixels, self.seconds_per_beat))
        f.add_follower_step(Step.Follow(Step.Foot.LEFT, self.seconds_per_beat))

        # Slow Waltz - Step 6
        f.add_leader_step(Step.Close(Step.Foot.LEFT, self.seconds_per_beat))
        f.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.seconds_per_beat))

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
            self.current_figure = self.Left_Box_Turn(self.seconds_per_beat)
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
