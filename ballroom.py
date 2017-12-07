import arcade
import datetime

import Dancer
import Step
import Menu
import Waltz
import Rumba

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768



class MyApplication(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)
                
        self.leader = Dancer.Dancer()
        self.follower = Dancer.Dancer()
        
        self.leader.load_supporting_foot_texture(Step.Foot.LEFT, "man_left_foot.jpg")
        self.leader.load_supporting_foot_texture(Step.Foot.RIGHT, "man_right_foot.jpg")
        self.leader.load_free_foot_texture(Step.Foot.LEFT, "man_left_free_foot.jpg")
        self.leader.load_free_foot_texture(Step.Foot.RIGHT, "man_right_free_foot.jpg")
        self.leader.set_free_foot(Step.Foot.LEFT)
        
        self.follower.load_supporting_foot_texture(Step.Foot.LEFT, "lady_left_foot.jpg")
        self.follower.load_supporting_foot_texture(Step.Foot.RIGHT, "lady_right_foot.jpg")
        self.follower.load_free_foot_texture(Step.Foot.LEFT, "lady_left_free_foot.jpg")
        self.follower.load_free_foot_texture(Step.Foot.RIGHT, "lady_right_free_foot.jpg")   
        self.follower.set_free_foot(Step.Foot.RIGHT)

        # eventually the user should be able to choose the start position
        self.leader.set_left_position(300, 120, 0)
        self.leader.set_right_position(400, 120, 0)
        self.follower.set_left_position(450, 300, 180)
        self.follower.set_right_position(350, 300, 180)
        
        self.menu = Menu.Menu()
            
        # Note:
        # You can change how often the animate() method is called by using the
        # set_update_rate() method in the parent class.
        # The default is once every 1/80 of a second.
        # self.set_update_rate(1/80)
        

    def load_figure(self, figure):        
        for step in figure.leader_steps:
            self.leader.add_step(step)
            
        for step in figure.follower_steps:
            self.follower.add_step(step) 

        
    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        
        # draw the menu
        self.menu.draw()

        # draw each dancer
        self.leader.draw()
        self.follower.draw()

        
    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        # update the position of each dancer        
        self.leader.update(delta_time)
        self.follower.update(delta_time)        


    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://pythonhosted.org/arcade/arcade.key.html
        """

        if key == arcade.key.ESCAPE:
            self.close()
            

        self.menu.process_key(key, key_modifiers)
        
        # see if user is done entering the routine, this should be a separate event
        if key == arcade.key.KEY_0:
            for fig in self.menu.current_routine:
                self.load_figure(fig)
                
        # see if user is ready to start, this should be a separate event
        if key == arcade.key.SPACE:
            self.leader.start_next_step()
            self.follower.start_next_step()

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.SPACE:
            print("You stopped pressing the space bar.")

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()