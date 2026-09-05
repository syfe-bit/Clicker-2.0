import arcade
import arcade.gui

import src.gameplay.coregameplay as coregameplay
import src.gameplay.calculateMoney as calculateMoney

TEX_RED_BUTTON_NORMAL = arcade.load_texture(":resources:gui_basic_assets/button/red_normal.png")
TEX_RED_BUTTON_HOVER = arcade.load_texture(":resources:gui_basic_assets/button/red_hover.png")
TEX_RED_BUTTON_PRESS = arcade.load_texture(":resources:gui_basic_assets/button/red_press.png")

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

## -----------------------------------------------------------------------------------

class CoreGamePlay(arcade.View):
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

        btn = arcade.gui.UIFlatButton(text=f"Bouton test", width=120)
        grid.add(btn, col_num=2, row_num=1)
        anchor = arcade.gui.UIAnchorLayout()
        anchor.add(child=grid,
                   anchor_x="left",
                   anchor_y="center",
                   align_x=20)
        self.ui.add(anchor)

        self.money = calculateMoney.Money()
        self.planets = arcade.SpriteList()
        self.display_money = arcade.Text(
            "money : 0",
            x=10,
            y=10,
            color=arcade.csscolor.WHITE,
            font_size=18,
        )

        ## -----------------------------------------------
        ## ---------------- system planet ----------------

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
        