import arcade

class Figure():
    # a Figure is a list of steps for both leader and follower

    def __init__(self, name):
        self.leader_steps = []
        self.follower_steps = []
        self.name = arcade.create_text(name, arcade.color.BLACK, 14)
        self.menu_items = []
        self.customization_needed = False

    def add_leader_step(self, s):
        self.leader_steps.append(s)

    def add_follower_step(self, s):
        self.follower_steps.append(s)

    def draw_name(self, x, y):
        arcade.render_text(self.name, x, y)

    def define_menu_item(self, item_text):
        self.menu_items.append(arcade.create_text(item_text, arcade.color.BLACK, 14))
        
    def clear_menu_items(self):
        self.menu_items.clear()

    def draw_menu_item(self, index, x, y):
        arcade.render_text(self.menu_items[index], x, y)

    def customize(self, index):
        pass
