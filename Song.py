import arcade

class Song():

    def __init__(self, filename, bpm, seek = 0):
        self.filename = filename
        self.bpm = bpm
        self.seek = seek
        # strip this down to the base filename
        self.menu_text = arcade.create_text(self.filename, arcade.color.BLACK, 14)

    def draw_menu_entry(self, x, y):
        arcade.render_text(self.menu_text, x, y)
