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
        self.planets.append(coregameplay.Sun(self.window_width, self.window_height, 1, 5))
        self.planets.append(coregameplay.Mercury(self.window_width * 1.1, self.window_height, -2, 3))
        self.planets.append(coregameplay.Venus(self.window_width * 1.2, self.window_height, -3, 4))
        self.planets.append(coregameplay.Earth(self.window_width * 1.3, self.window_height, -3.5, 4.5))
        self.planets.append(coregameplay.Mars(self.window_width * 1.4, self.window_height, -3.6, 4.6))
        self.planets.append(coregameplay.Jupiter(self.window_width * 1.5, self.window_height, -3.7, 4.7))
        self.planets.append(coregameplay.Saturn(self.window_width * 1.6, self.window_height, -3.8, 4.8))
        self.planets.append(coregameplay.Uranus(self.window_width * 1.7, self.window_height, -3.9, 4.9))
        self.planets.append(coregameplay.Neptune(self.window_width * 1.8, self.window_height, -4, 5))
        

    def on_draw(self):
        self.clear()
        self.planets.draw()
        
    
    def on_update(self, delta_time):
        self.planets.update()
        