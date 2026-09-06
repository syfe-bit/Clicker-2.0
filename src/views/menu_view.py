import arcade

import src.views.game_view as game_view

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.window = arcade.get_window()
        self.background_color = arcade.color.AMAZON

    def on_draw(self):
        self.clear()
        arcade.Text("Clique pour jouer", 400, 300, arcade.color.WHITE, 20).draw()

    def on_mouse_press(self, x, y, button, modifiers):
        self.window.show_view(game_view.GameView())