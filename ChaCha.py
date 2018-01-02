import Step
import Dance
from Figure import Figure
import Song
import arcade
import pyglet

class ChaCha(Dance.Dance):

    def __init__(self):
        super().__init__()
        self.beats_per_minute = 120   # BPM should come from song
        self.seconds_per_beat = 60 / self.beats_per_minute
        self.name = arcade.create_text("C: Cha Cha", arcade.color.BLACK, 14)

    class Basic(Figure):
        def __init__(self, timing):
            super().__init__("Basic Movement")
            self.customization_needed = True
            self.customization_count = 0
            self.define_menu_item("a. Prep Step Needed")
            self.define_menu_item("b. No Prep Step")
            self.beat_time = timing

        def customize(self, index):
            self.customization_count += 1
            if self.customization_count == 1:
                self.forward_pixels = 80
                self.side_pixels = 60
                if index == 0:
                    self.prep_step_needed = True
                else:
                    self.prep_step_needed = False
                self.clear_menu_items()
                self.define_menu_item("a: Side Chasses")
                self.define_menu_item("b: Progressive Chasses")
            else:
                if index == 0:
                    self.progressive = False
                else:
                    self.progressive = True

                if self.prep_step_needed:
                    # Prep Step - Side
                    self.add_leader_step(Step.Side(Step.Foot.RIGHT, self.side_pixels * 0.5, self.beat_time))
                    self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time))

                # Count 2, Step 1 - Forward Rock
                self.add_leader_step(Step.Forward(Step.Foot.LEFT, self.forward_pixels, self.beat_time))
                self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time))

                # Count 3, Step 2 - Replace Weight
                self.add_leader_step(Step.Step(Step.Foot.RIGHT, self.beat_time))
                self.add_follower_step(Step.Step(Step.Foot.LEFT, self.beat_time))

                # Count 4 and 1 - Steps 3-5 Chasse
                if self.progressive:
                    self.add_leader_step(Step.Backward(Step.Foot.LEFT, self.forward_pixels, self.beat_time * 0.5))
                    self.add_leader_step(Step.Close(Step.Foot.RIGHT, self.beat_time * 0.5))
                    self.add_leader_step(Step.Backward(Step.Foot.LEFT, self.forward_pixels, self.beat_time))
                else:
                    self.add_leader_step(Step.Side(Step.Foot.LEFT, -self.side_pixels, self.beat_time * 0.5))
                    self.add_leader_step(Step.Close(Step.Foot.RIGHT, self.beat_time * 0.5))
                    self.add_leader_step(Step.Side(Step.Foot.LEFT, -self.side_pixels, self.beat_time))

                self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time * 0.5))
                self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time * 0.5))
                self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time))

                # Count 2, Step 6 - Forward Rock
                self.add_leader_step(Step.Backward(Step.Foot.RIGHT, self.forward_pixels, self.beat_time))
                self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time))

                # Count 3, Step 7 - Replace Weight
                self.add_leader_step(Step.Step(Step.Foot.LEFT, self.beat_time))
                self.add_follower_step(Step.Step(Step.Foot.RIGHT, self.beat_time))

                # Count 4 and 1 - Steps 8-10 Chasse Right
                if self.progressive:
                    self.add_leader_step(Step.Forward(Step.Foot.RIGHT, self.forward_pixels, self.beat_time * 0.5))
                    self.add_leader_step(Step.Close(Step.Foot.LEFT, self.beat_time * 0.5))
                    self.add_leader_step(Step.Forward(Step.Foot.RIGHT, self.forward_pixels, self.beat_time))
                else:
                    self.add_leader_step(Step.Side(Step.Foot.RIGHT, self.side_pixels, self.beat_time * 0.5))
                    self.add_leader_step(Step.Close(Step.Foot.LEFT, self.beat_time * 0.5))
                    self.add_leader_step(Step.Side(Step.Foot.RIGHT, self.side_pixels, self.beat_time))

                self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time * 0.5))
                self.add_follower_step(Step.Follow(Step.Foot.RIGHT, self.beat_time * 0.5))
                self.add_follower_step(Step.Follow(Step.Foot.LEFT, self.beat_time))

                self.customization_needed = False

    def load_figure_names(self):
        self.figure_names.append(arcade.create_text("1: Basic", arcade.color.BLACK, 14))

    def select_figure(self, index):
        if index == 0:
            self.current_figure = self.Basic(self.seconds_per_beat)
        if not self.current_figure.customization_needed:
            self.current_routine.append(self.current_figure)
        return self.current_figure

    def load_songs(self):
        self.song_list.append(Song.Song(1, "Music/ChaCha/Smooth.mp3", 120))
