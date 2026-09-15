import arcade
import arcade.gui

class RemainingButton(arcade.gui.UIFlatButton):
    def __init__(self, button_name, callback=None, **kwargs):
        self.button_name = button_name
        self.callback = callback

        super().__init__(
            text=f"{self.button_name}",
            width=200, 
            height=60,
            **kwargs
        )

        if callback:
            self.on_click = callback