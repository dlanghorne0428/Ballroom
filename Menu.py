from enum import IntEnum
import arcade

import Dance
import Waltz
import Tango
import Foxtrot
import ChaCha
import Rumba
import EastCoastSwing

class MenuState(IntEnum):
    SELECT_DANCE = 0
    SELECT_SONG = 1
    SELECT_FIGURE = 2
    CUSTOMIZE_FIGURE = 3
    READY_TO_START = 4
    DANCING = 5


class Menu():

    def __init__(self):
        self.current_state = MenuState.SELECT_DANCE
        self.dance_menu = []
        self.dance_menu.append(Waltz.Waltz())
        self.dance_menu.append(Tango.Tango())
        self.dance_menu.append(Foxtrot.Foxtrot())
        self.dance_menu.append(ChaCha.ChaCha())
        self.dance_menu.append(Rumba.Rumba())
        self.dance_menu.append(EastCoastSwing.East_Coast_Swing())
        # more dances go here

        self.current_dance = None

        self.dance_prompt = arcade.create_text("SELECT A DANCE", arcade.color.BLACK, 14, bold=True)
        self.song_prompt = arcade.create_text("Select a song", arcade.color.BLACK, 14, bold=True, italic=True)
        self.routine_prompt = arcade.create_text("Create a routine", arcade.color.BLACK, 14, bold=True, italic=True)
        self.avail_prompt = arcade.create_text("Available Figures", arcade.color.BLACK, 14, bold=True, italic=True)
        self.done_prompt = arcade.create_text("0: Stop adding figures", arcade.color.BLACK, 14)
        self.silent_prompt = arcade.create_text("0: No music", arcade.color.BLACK, 14)
        self.start_prompt = arcade.create_text("Press space bar to start", arcade.color.BLACK, 14)
        self.customize_prompt = arcade.create_text("Customize Figure", arcade.color.BLACK, 14, bold=True, italic=True)


    def draw(self):
        if self.current_state == MenuState.SELECT_DANCE:
            arcade.render_text(self.dance_prompt, 50, 500)
            index = 0
            while index < len(self.dance_menu):
                d = self.dance_menu[index]
                d.draw_name(50, 480-index*20)
                index += 1

        elif self.current_state == MenuState.SELECT_SONG:
            self.current_dance.draw_name(50, 500)
            arcade.render_text(self.song_prompt, 50, 480)
            index = 0
            while index < len(self.current_dance.song_list):
                s = self.current_dance.song_list[index]
                s.draw_menu_entry(50, 460-index*20)
                index += 1

            arcade.render_text(self.silent_prompt, 50, 420-(index)*20)


        elif self.current_state == MenuState.SELECT_FIGURE:
            self.current_dance.draw_name(50, 500)
            arcade.render_text(self.routine_prompt, 50, 480)

            routine_index = 0
            r = self.current_dance.current_routine
            while routine_index < len(r):
                fig = r[routine_index]
                fig.draw_name(50, 460-routine_index*20)
                routine_index += 1

            arcade.render_text(self.avail_prompt, 50, 440-routine_index*20)
            figure_index = 0
            while figure_index < len(self.current_dance.figure_names):
                name = self.current_dance.figure_names[figure_index]
                arcade.render_text(name, 50, 420-(figure_index+routine_index)*20)
                figure_index += 1

            arcade.render_text(self.done_prompt, 50, 400-(figure_index+routine_index)*20)

        elif self.current_state == MenuState.CUSTOMIZE_FIGURE:
            self.current_dance.draw_name(50, 500)
            arcade.render_text(self.routine_prompt, 50, 480)

            routine_index = 0
            r = self.current_dance.current_routine
            while routine_index < len(r):
                fig = r[routine_index]
                fig.draw_name(50, 460-routine_index*20)
                routine_index += 1

            f = self.current_dance.current_figure
            f.draw_name(50, 460-routine_index*20)
            arcade.render_text(self.customize_prompt, 50, 440-routine_index*20)
            custom_index = 0
            while custom_index < len(f.menu_items):
                f.draw_menu_item(custom_index, 50, 420-(custom_index+routine_index)*20)
                custom_index += 1

        elif self.current_state == MenuState.READY_TO_START:
            self.current_dance.draw_name(50, 500)
            arcade.render_text(self.start_prompt, 50, 460)
        elif self.current_state == MenuState.DANCING:
            self.current_dance.draw_name(50, 500)


    def process_key(self, key, key_modifiers):

        if self.current_state == MenuState.SELECT_DANCE:
            if key == arcade.key.W:
                print("You selected Waltz")
                self.current_dance = self.dance_menu[0]
            elif key == arcade.key.F:
                print("You selected Foxtrot")
                self.current_dance = self.dance_menu[2]
            elif key == arcade.key.R:
                print("You selected Rumba")
                self.current_dance = self.dance_menu[4]  # this should be based on name somehow
            else:
                print("Please select a dance from the menu")

            if self.current_dance is None:
                pass
            else:
                self.current_state = MenuState.SELECT_SONG
                self.current_dance.initialize_dancers()
                self.current_dance.load_songs()

        elif self.current_state == MenuState.SELECT_SONG:
            if key >= arcade.key.KEY_1 and key <= arcade.key.KEY_9:
                index = key - arcade.key.KEY_1
                if index < len(self.current_dance.song_list):
                    self.current_dance.select_song(index)
                    self.current_state = MenuState.SELECT_FIGURE
                    self.current_dance.load_figure_names()
                    self.current_dance.current_figure = None
            elif key == arcade.key.KEY_0:
                self.current_state = MenuState.SELECT_FIGURE
                self.current_dance.load_figure_names()
                self.current_dance.current_figure = None

        elif self.current_state == MenuState.SELECT_FIGURE:
            if key >= arcade.key.KEY_1 and key <= arcade.key.KEY_9:
                index = key - arcade.key.KEY_1
                if index < len(self.current_dance.figure_names):
                    f = self.current_dance.select_figure(index)
                    if f.customization_needed:
                        self.current_state = MenuState.CUSTOMIZE_FIGURE
            elif key == arcade.key.KEY_0:
                if len(self.current_dance.current_routine) > 0:
                    self.current_state = MenuState.READY_TO_START
                    self.current_dance.prepare_dancers()

        elif self.current_state == MenuState.CUSTOMIZE_FIGURE:
            if key >= arcade.key.A and key <= arcade.key.Z:
                index = key - arcade.key.A
                f = self.current_dance.current_figure
                if index < len(f.menu_items):
                    self.current_dance.customize_current_figure(index)
                    self.current_state = MenuState.SELECT_FIGURE

        # See if the user just hit space.
        elif self.current_state == MenuState.READY_TO_START:
            if key == arcade.key.SPACE:
                print("You pressed the space bar - Dance is starting.")
                self.current_state = MenuState.DANCING
                self.current_dance.start_dance()
                if self.current_dance.current_song is not None:
                    self.current_dance.play_song()

        elif self.current_state == MenuState.DANCING:
            pass
            # what to do here?

