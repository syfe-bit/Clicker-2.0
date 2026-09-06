import arcade

import src.views.menu_view as menu_view

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "CLICKER PIXEL"

def main():
    Window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    Window.show_view(menu_view.MenuView())
    arcade.run()

if __name__ == "__main__":
    main()