import arcade
import arcade.gui

from src.ui import (dropdown, remainingButtons)

class settings_view():
    def __init__(self):
        self.windows = arcade.get_window()
        self.window_width = self.windows.width //2
        self.window_height = self.windows.height //2

        self.ui_manager = arcade.gui.UIManager()

        store_button_box = arcade.gui.UIBoxLayout(space_between=10)

        perso_dropdown = dropdown.Dropdown_resolution(default="default", options=["1280x720", "1600x900", "1920x1080", "2560x1440", "3840x2160"])

        store_button_box.add(perso_dropdown)
          
        anchor_for_the_store_button_box = arcade.gui.UIAnchorLayout()
        anchor_for_the_store_button_box.add(
            child=store_button_box,
            anchor_x="left",
            anchor_y="center",
            align_x=20,
        )
        self.ui_manager.add(anchor_for_the_store_button_box)

    def on_show_view(self):
        self.ui_manager.enable()
    
    def on_hide_view(self):
        self.ui_manager.disable()

    def on_draw(self):
        arcade.draw_rect_filled(
            arcade.XYWH(self.window_width, self.window_height, self.windows.width, self.windows.height),
            color=(0, 0, 0, 255)
        )
        self.ui_manager.draw()

    

