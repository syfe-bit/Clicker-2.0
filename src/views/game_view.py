import arcade
import arcade.gui
import arcade.types

from src.ui.buttons import ShopButton

import src.game.coregameplay as coregameplay
import src.game.calculateMoney as calculateMoney

## -----------------------------------------------------------------------------------



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
        box = arcade.gui.UIBoxLayout(space_between=10)

        self.shop_buttons = []
        for i in range(9):
            btn = ShopButton(initial_price=100, unlock_amount=10*i, callback=None)
            btn.callback = lambda e, b=btn: self.buy_upgrade(b)
            btn.on_click = btn.callback
            self.shop_buttons.append(btn)
            box.add(btn)

        anchor = arcade.gui.UIAnchorLayout()
        anchor.add(child=box,
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
        self.display_money.text = f"money: {self.money.get_money():.2f}"
        self.display_money.draw()
        self.planets.draw()
        
    def on_update(self, delta_time):
        self.planets.update()
        for btn in self.shop_buttons:
            btn.update_visibility(self.money.get_money())

    def buy_upgrade(self, btn):
        if self.money.get_money() >= btn.price:
            if self.money.withdraw_money(btn.price):
                btn.update_price((btn.price * 1.15))
                print(f"Achat réussi ! Prix suivant : {btn.price}$")
        