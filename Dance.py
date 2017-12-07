import arcade
import pyglet

class Dance():
    
    def __init__(self):
        self.figure_list = []
        self.song_list = []
        self.name = None
        self.current_figure = None
        self.current_song = None
        self.player = None
        
    def get_figure(self, index):
        self.current_figure = self.figure_list[index]
        return self.current_figure
    
    def draw_name(self, x, y):
        if self.name is None:
            pass
        else:
            arcade.render_text(self.name, x, y)
            
    def select_song(self, index):
        self.current_song = self.song_list[index]
        
    def play_song(self):
        from pyglet.media.player import Player
        if self.player is None:
            self.player = pyglet.media.Player()
        if not self.player.playing:
            self.player.queue(self.current_song)
            self.player.play()
        # arcade.sound.play_sound(self.current_song)