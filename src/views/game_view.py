import arcade
import arcade.gui
import arcade.types

import src.game.coregameplay as coregameplay
import src.game.calculateMoney as calculateMoney

## -----------------------------------------------------------------------------------

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        windows = arcade.get_window()
        self.window_width = windows.width //2
        self.window_height = windows.height //2
        self.background_color = arcade.color.RED_DEVIL

        ## -----------------------------------------------
        ## ---------------- system button ----------------

        self.ui = arcade.gui.UIManager()
        grid = arcade.gui.UIGridLayout(
                    column_count=9,
                    row_count=1,
                    vertical_spacing=10,
                    horizontal_spacing=10,
        )

        self.btn = arcade.gui.UITextureButton(texture=arcade.load_texture("sprites/button/button_market_sun.png"), text="test", scale=3)
        grid.add(self.btn, col_num=2, row_num=0)

        anchor = arcade.gui.UIAnchorLayout()
        anchor.add(child=grid,
                   anchor_x="left",
                   anchor_y="center",
                   align_x=20)
        self.ui.add(anchor)

        ## -----------------------------------------------
        ## ------------- cash display system -------------

        self.money = calculateMoney.Money()
        self.display_money = arcade.Text(
            "money : 0",
            x=10,
            y=10,
            color=arcade.csscolor.WHITE,
            font_size=18,
        )

        ## -----------------------------------------------
        ## ---------------- system planet ----------------

        self.planets = arcade.SpriteList()
        self.sun = coregameplay.Sun(self.window_width, self.window_height, 1, 5, self.money)
        self.planets.append(self.sun)
        ##self.planets.append(coregameplay.Mercury(self.window_width * 1.1, self.window_height, -2, 3))
        ##self.planets.append(coregameplay.Venus(self.window_width * 1.2, self.window_height, -3, 4))
        ##self.planets.append(coregameplay.Earth(self.window_width * 1.3, self.window_height, -3.5, 4.5))
        ##self.planets.append(coregameplay.Mars(self.window_width * 1.4, self.window_height, -3.6, 4.6))
        ##self.planets.append(coregameplay.Jupiter(self.window_width * 1.5, self.window_height, -3.7, 4.7))
        ##self.planets.append(coregameplay.Saturn(self.window_width * 1.6, self.window_height, -3.8, 4.8))
        ##self.planets.append(coregameplay.Uranus(self.window_width * 1.7, self.window_height, -3.9, 4.9))
        ##self.planets.append(coregameplay.Neptune(self.window_width * 1.8, self.window_height, -4, 5))
        
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.sun.Click_to_update()

    def on_show_view(self):
        self.ui.enable()

    def on_hide_view(self):
        self.ui.disable()

    def on_draw(self):
        self.clear()
        self.ui.draw()
        self.display_money.text = f"money: {self.money.get_money()}"
        self.display_money.draw()
        self.planets.draw()
        
    def on_update(self, delta_time):
        self.planets.update()
        if self.money.get_money() > 20:
            self.btn.disabled = False
        else:
            self.btn.disabled = True
        