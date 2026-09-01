import arcade

import src.gameplay.coregameplay as coregameplay

class HomeMenu(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.AMAZON

    def on_draw(self):
        self.clear()
        arcade.Text("Clique pour jouer", 400, 300, arcade.color.WHITE, 20).draw()

    def on_mouse_press(self, x, y, button, modifiers):
        game_view = CoreGamePlay()
        self.window.show_view(game_view)

class CoreGamePlay(arcade.View):
    def __init__(self):
        super().__init__()
        windows = arcade.get_window()
        self.window_width = windows.width //2
        self.window_height = windows.height //2
        self.background_color = arcade.color.RED_DEVIL
        self.planets = arcade.SpriteList()
        self.planets.append(coregameplay.Sun(self.window_width, self.window_height))
        self.planets.append(coregameplay.Mercury(self.window_width * 1.2, self.window_height))
        

    def on_draw(self):
        self.clear()
        self.planets.draw()
        
    
    def on_update(self, delta_time):
        self.planets.update(delta_time * 60)
        