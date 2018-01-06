import Step
import Dance
from Figure import Figure
import Song
import arcade
import pyglet

class Tango(Dance.Dance):

    def __init__(self):
        super().__init__()
        self.beats_per_minute = 120   # BPM should come from song
        self.seconds_per_beat = 60 / self.beats_per_minute
        self.name = arcade.create_text("T: Tango", arcade.color.BLACK, 24)

    class Count_8_Basic(Figure):
        def __init__(self, timing):
            super().__init__("8-count Basic")
            self.customization_needed = True
            self.customization_count = 0
            self.define_menu_item("a. No Turn")
            self.define_menu_item("b. Slight Left Turn")
            self.beat_time = timing

        def customize(self, index):
            self.customization_count += 1
            if self.customization_count == 1:
                self.forward_pixels = 120
                self.side_pixels = 80
                if index == 0:
                    self.rot_angle = 0
                else:
                    self.rot_angle = 10

                # Step 1 - Walk Forward
                self.add_leader_step(Step.Forward(Step.Foot.LEFT, self.forward_pixels, 2 * self.beat_time, rotation=self.rot_angle))
                self.add_follower_step(Step.Follow(Step.Foot.RIGHT, 2 * self.beat_time))

                # Step 2, Walk Forward
                self.add_leader_step(Step.Forward(Step.Foot.RIGHT, self.forward_pixels, 2 * self.beat_time, rotation=self.rot_angle))
                self.add_follower_step(Step.Follow(Step.Foot.LEFT, 2 * self.beat_time))

                # Step 3 - Walk Forward Quick - TAN
                self.add_leader_step(Step.Forward(Step.Foot.LEFT, self.forward_pixels, self.beat_time, rotation=self.rot_angle))
                self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time))

                # Step 4 - Side Quick - GO
                self.add_leader_step(Step.Side(Step.Foot.RIGHT, self.side_pixels, self.beat_time))
                self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time))

                # Step 5 - slow - CLOSE
                self.add_leader_step(Step.Close(Step.Foot.LEFT, 2 * self.beat_time))
                self.add_follower_step(Step.Follow(Step.Foot.RIGHT, 2 * self.beat_time))

                self.customization_needed = False


    def load_figure_names(self):
        self.figure_names.append(arcade.create_text("1: 8 Count Basic", arcade.color.BLACK, 14))

    def select_figure(self, index):
        if index == 0:
            self.current_figure = self.Count_8_Basic(self.seconds_per_beat)
        if not self.current_figure.customization_needed:
            self.current_routine.append(self.current_figure)
        return self.current_figure

    def load_songs(self):
        self.song_list.append(Song.Song(1, "Music/Tango/Santa Maria.mp3", 118))
