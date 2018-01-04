import Step
import Dance
from Figure import Figure
import Song
import arcade
import pyglet

class East_Coast_Swing(Dance.Dance):

    def __init__(self):
        super().__init__()
        self.beats_per_minute = 144   # BPM should come from song
        self.seconds_per_beat = 60 / self.beats_per_minute
        self.name = arcade.create_text("E: East Coast Swing", arcade.color.BLACK, 14)

    class Basic_Step(Figure):
        def __init__(self, timing):
            super().__init__("Basic Step")
            self.customization_needed = True
            self.customization_count = 0
            self.define_menu_item("a. No Turn")
            self.define_menu_item("b. 1/8 Turn - Left")
            self.define_menu_item("c. 1/4 Turn - Left")
            self.beat_time = timing

        def customize(self, index):
            self.customization_count += 1
            if self.customization_count == 1:
                self.forward_pixels = 80
                self.side_pixels = 80
                if index == 0:
                    self.pivot = 0
                elif index == 1:
                    self.pivot = 15
                else:
                    self.pivot = 30

                # Steps 1 - 3 Triple Step Left
                self.add_leader_step(Step.Side(Step.Foot.LEFT, -self.side_pixels * 0.5, self.beat_time * 0.5, pre_step_pivot=self.pivot))
                self.add_leader_step(Step.Close(Step.Foot.RIGHT, self.beat_time * 0.5))
                self.add_leader_step(Step.Side(Step.Foot.LEFT, -self.side_pixels, self.beat_time))

                self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time * 0.5))
                self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time * 0.5))
                self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time))

                # Steps 4 - 6 Triple Step Right
                self.add_leader_step(Step.Side(Step.Foot.RIGHT, self.side_pixels * 0.75, self.beat_time * 0.5, pre_step_pivot=self.pivot))
                self.add_leader_step(Step.Close(Step.Foot.LEFT, self.beat_time * 0.5))
                self.add_leader_step(Step.Side(Step.Foot.RIGHT, self.side_pixels * 0.75, self.beat_time))

                self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time * 0.5))
                self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time * 0.5))
                self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time))

                # Steps 7 - 8 Rock Back, Replace
                self.add_leader_step(Step.Backward(Step.Foot.LEFT, self.forward_pixels, self.beat_time, pre_step_pivot=30+self.pivot))
                self.add_leader_step(Step.Step(Step.Foot.RIGHT, self.beat_time))
                self.add_follower_step(Step.Backward(Step.Foot.RIGHT, self.forward_pixels, self.beat_time, pre_step_pivot=-30+self.pivot))
                self.add_follower_step(Step.Step(Step.Foot.LEFT, self.beat_time))

                self.customization_needed = False

    def load_figure_names(self):
        self.figure_names.append(arcade.create_text("1: Basic Step", arcade.color.BLACK, 14))

    def select_figure(self, index):
        if index == 0:
            self.current_figure = self.Basic_Step(self.seconds_per_beat)
        if not self.current_figure.customization_needed:
            self.current_routine.append(self.current_figure)
        return self.current_figure

    def load_songs(self):
        self.song_list.append(Song.Song(1, "Music/EastCoast/Long Cool Woman.mp3", 139))
        self.song_list.append(Song.Song(2, "Music/EastCoast/Tush.mp3", 145))
