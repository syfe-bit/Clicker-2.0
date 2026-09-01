import arcade

import src.display as display

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "CLICKER PIXEL"

def main():
    Window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    Window.show_view(display.HomeMenu())
    arcade.run()

if __name__ == "__main__":
    main()