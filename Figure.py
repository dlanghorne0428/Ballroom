"""
The Figure module contains a base class for defining figures from the syllabus
"""
import arcade

class Figure():
    """
    A Figure is a list of steps for both leader and follower.
    This is a base class. Derived classes will be in each Dance.
    """

    def __init__(self, name):
        """ Initialize the base class with the name of the figure."""
        self.leader_steps = []     # start with empty list of steps
        self.follower_steps = []
        # the figure name can be rendered and displayed on the screen
        self.name = arcade.create_text(name, arcade.color.BLACK, 14)
        # Figures can be customized from a menu of options
        self.menu_items = []      # start with an empty list of options
        self.customization_needed = False  # indicate if more customization is needed

    def add_leader_step(self, s):
        self.leader_steps.append(s)

    def add_follower_step(self, s):
        self.follower_steps.append(s)

    def draw_name(self, x, y):
        """ render the nae of the figure at the given (x,y) position. """
        arcade.render_text(self.name, x, y)

    def define_menu_item(self, item_text):
        """ add an item to the customization menu """
        self.menu_items.append(arcade.create_text(item_text, arcade.color.BLACK, 14))

    def clear_menu_items(self):
        self.menu_items.clear()   # remove all items from the customization menu

    def draw_menu_item(self, index, x, y):
        """ render the menu item at the given (x,y) position. """
        arcade.render_text(self.menu_items[index], x, y)

    def customize(self, index):
        """ define an abstract method for selecting an option from the customization menu """
        pass
