import arcade
import arcade.gui

class Dropdown_resolution(arcade.gui.UIDropdown):
    def __init__(self, default: str, options: list[str], **kwargs):
        super().__init__(
            default=default,
            options=options,
            width=200, 
            height=60,
            **kwargs
        )

        @self.event("on_change")
        def on_change(event):
            window = arcade.get_window()
            resolution = event.new_value
            list_of_resolution_sizes = resolution.split(sep="x")
            window.width = int(list_of_resolution_sizes[0])
            window.height = int(list_of_resolution_sizes[1])
            