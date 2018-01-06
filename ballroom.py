""" This is the main program for the Ballroom Dance application. """
import arcade
import datetime

import Dancer
import Step
import Menu
import Waltz
import Rumba
import pyglet

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768



class MyApplication(arcade.Window):
    """
    We use the Arcade library.
    This class is the standard application class for Arcade.
    It controls the main window.
    It declares two Dancer objects and a Menu object.
    """

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)

        # declare the two dancers
        #self.leader = Dancer.Dancer()
        #self.follower = Dancer.Dancer()

        # declare the menu
        self.menu = Menu.Menu()
        pyglet.options['search_local_libs'] = True
        pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')


    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        self.menu.draw()
        if self.menu.current_dance is not None:
            self.menu.current_dance.draw_dancers()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        # update the position of each dancer
        if self.menu.current_dance is not None:
            dance_in_progress = self.menu.current_dance.update_dancers(delta_time)

        # see if dance has finished
        if (self.menu.current_state == Menu.MenuState.DANCING and
            not dance_in_progress):
            self.menu.current_dance.pause_song()
            self.menu.current_state = Menu.MenuState.SELECT_FIGURE


    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcadeacademy.org/arcade/arcade.key.html
        """

        if key == arcade.key.ESCAPE:
            self.close()

        self.menu.process_key(key, key_modifiers)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        """
        Called whenever the user scrolls the mouse.
        Need to override this, otherwise it will generate tracebacks.
        """
        pass

def main():
    """ Main method """
    MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
