import arcade
import arcade.gui as ui

class Settings_view():
    def __init__(self, anchor):

        ## -----------------------------------------------
        ## -------------- manage the widget --------------

        settings_buttons_grid = ui.UIGridLayout(size_hint=(1, 1), space_between=10, column_count= 2, row_count=3)
        settings_buttons_grid.with_padding(all=50)
        anchor.add(settings_buttons_grid)
        
        ## -----------------------------------------------
        ## -------------- resolution widget --------------
        
        dropdown_resolution_box = ui.UIBoxLayout(vertical=False, space_between=40)
        settings_buttons_grid.add(dropdown_resolution_box, column= 0, row= 0)
        dropdown_resolution_box.add(ui.UILabel(text="Screen resolution", font_size=20, size_hint=(1, 1)))
        dropdown_resolution = ui.UIDropdown(
                        default="default", 
                        options=["1280x720", "1600x900", "1920x1080", "2560x1440", "3840x2160"]
                    )

        @dropdown_resolution.event()
        def on_change(event):
            window = arcade.get_window()
            resolution = event.new_value
            list_of_resolution_sizes = resolution.split(sep="x")
            window.set_size(int(list_of_resolution_sizes[0]), int(list_of_resolution_sizes[1]))

        dropdown_resolution_box.add(dropdown_resolution)

        ## -----------------------------------------------
        ## --------------- language widget ---------------

        dropdown_sreen_mode_box = ui.UIBoxLayout(vertical=False, space_between=40)
        settings_buttons_grid.add(dropdown_sreen_mode_box, column=0, row=1)
        dropdown_sreen_mode_box.add(ui.UILabel(text="Screen mode", font_size=20))
        dropdown_sreen_mode = ui.UIDropdown(
            default="default",
            options=["Window", "Full screen"]
        )

        @dropdown_sreen_mode.event()
        def on_change(event):
            window = arcade.get_window()
            if event.new_value == "Full screen":
                window.set_fullscreen(fullscreen=True)
            else:
                window.set_fullscreen(fullscreen=False)

        dropdown_sreen_mode_box.add(dropdown_sreen_mode)

        ## -----------------------------------------------
        ## -------------- screen mode widget -------------
    

