import arcade
import arcade.gui

from src.ui import (shopButtons, remainingButtons)

from src.game.coregameplay import (sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune)
from src.game.upgrade.upgrade import Upgrade
import src.game.calculateMoney as calculateMoney

## -----------------------------------------------------------------------------------

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        windows = arcade.get_window()
        self.window_width = windows.width //2
        self.window_height = windows.height //2
        self.background_color = arcade.color.RED_DEVIL

        self.settings_open = False

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

        # (classe, décalage_x, orbit_speed, rotation_angle, money_value, initial_price)
        planet_configs = [
            (sun.Sun, 1.0, 1, 1, 10, 20),
            (mercury.Mercury, 1.1, 1, 1, 20, 40),
            (venus.Venus, 1.2, 1, 1, 30, 80),
            (earth.Earth, 1.3, 1, 1, 40, 160),
            (mars.Mars, 1.4, 1, 1, 50, 320),
            (jupiter.Jupiter, 1.5, 1, 1, 60, 640),
            (saturn.Saturn, 1.6, 1, 1, 70, 1280),
            (uranus.Uranus, 1.7, 1, 1, 80, 2560),
            (neptune.Neptune, 1.8, 1, 1, 90, 5120)
        ]

        self.planets = arcade.SpriteList()
        self.planet_upgrades = []  # liste de (planet, upgrade)

        for planet_class, x_mult, orbit_speed, rotation_angle, money_value, initial_price in planet_configs:
            upgrade = Upgrade(initial_price=initial_price)
            planet = planet_class(
                x=self.window_width * x_mult,
                y=self.window_height,
                orbit_speed=orbit_speed,
                rotation_angle=rotation_angle,
                money=self.money,
                money_value=money_value,
                nb_of_times_purchased_upgrade=upgrade
            )
            self.planets.append(planet)
            self.planet_upgrades.append((planet, upgrade))

        self.sun = self.planets[0]

        ## -----------------------------------------------
        ## --------- Button system for the store ---------
        
        self.ui_manager = arcade.gui.UIManager()
        store_button_box = arcade.gui.UIBoxLayout(space_between=10)
        
        self.shop_buttons = []
        for i, (planet, upgrade) in enumerate(self.planet_upgrades):
            previous_upgrade = self.planet_upgrades[i-1][1] if i != 0 else None
            btn = shopButtons.ShopButton(
                initial_price=upgrade.price,
                number_of_upgrades_to_from_the_previous_planet=previous_upgrade,
                number_of_upgrades_to_unlock=0 if i == 0 else 10,
                callback=None
            )
            btn.callback = lambda e, p=planet, u=upgrade, b=btn: self.buy_upgrade(p, u, b)
            btn.on_click = btn.callback
            self.shop_buttons.append(btn)
            store_button_box.add(btn)
        
        anchor_for_the_store_button_box = arcade.gui.UIAnchorLayout()
        anchor_for_the_store_button_box.add(
            child=store_button_box,
            anchor_x="left",
            anchor_y="center",
            align_x=20,
        )
        self.ui_manager.add(anchor_for_the_store_button_box)

    ## -----------------------------------------------
    ## --------- Button system for the rest ---------
        
        box_for_the_remaining_buttons = arcade.gui.UIBoxLayout(space_between=10)

        remaining_buttons_configs = [
                    ("Sol", None),
                    ("settings", None)
                ]

        self.remaining_buttons = []
        for button_name, callback in remaining_buttons_configs:
            btn = remainingButtons.RemainingButton(button_name=button_name, callback=callback)
            self.remaining_buttons.append(btn)
            box_for_the_remaining_buttons.add(btn)

        anchor_for_the_layout_of_the_remaining_buttons = arcade.gui.UIAnchorLayout()
        anchor_for_the_layout_of_the_remaining_buttons.add(
            child=box_for_the_remaining_buttons,
            anchor_x="right",
            anchor_y="center",
            align_x=-20,
        )
        self.ui_manager.add(anchor_for_the_layout_of_the_remaining_buttons)
        
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.sun.Click_to_update()

    def on_show_view(self):
        self.ui_manager.enable()

    def on_hide_view(self):
        self.ui_manager.disable()

    def on_draw(self):
        self.clear()
        self.ui_manager.draw()
        self.display_money.text = f"money: {self.money.get_money():.2f}"
        self.display_money.draw()
        self.planets.draw()
        
    def on_update(self, delta_time):
        self.planets.update()
        for btn in self.shop_buttons:
            btn.update_visibility()

    def buy_upgrade(self, planet, upgrade, btn):
        if self.money.withdraw_money(btn.price):
            upgrade.add_nb_of_times_purchased_upgrade()
            upgrade.add_effect()
            speed_effect, money_multiplier_effect = upgrade.get_effect()
            planet.apply_effect_speed(speed_effect)
            planet.apply_effect_money(money_multiplier_effect)
            planet.apply_automation()
            btn.update_price((btn.price * 1.15))
        