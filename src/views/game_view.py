import arcade
import arcade.gui as ui

from src.ui import (shopButtons)

from src.game.coregameplay import (sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune)
from src.game.upgrade.upgrade import Upgrade
from src.views import (settings_view, sol_view)
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
        ## --------- Widget manager configuration --------

        self.ui_manager = ui.UIManager()
        main_anchor = ui.UIAnchorLayout()

        ## -----------------------------------------------
        ## ----- Anchor configuration for the banner -----

        banner_anchor = ui.UIAnchorLayout(size_hint=(1, 0.1))
        banner_anchor.with_background(color=arcade.color.PURPLE)
        main_anchor.add(banner_anchor, anchor_x="left", anchor_y="top")

        ## -----------------------------------------------
        ## ---- Anchor configuration for the content -----

        content_anchor = ui.UIAnchorLayout(size_hint=(0.7, 0.9))
        main_anchor.add(content_anchor, anchor_x="left", anchor_y="bottom")

        ## -----------------------------------------------
        ## ----------- Game view configuration -----------

        self.game_panel = ui.UIAnchorLayout(size_hint=(1, 1))
        content_anchor.add(self.game_panel, anchor_x="left", anchor_y="top")

        ## -----------------------------------------------
        ## ----------- Sol view configuration ------------

        self.sol_panel = ui.UIAnchorLayout(size_hint=(1, 1))
        self.sol_panel.with_background(color=arcade.uicolor.DARK_BLUE_MIDNIGHT_BLUE)
        content_anchor.add(self.sol_panel, anchor_x="left", anchor_y="top")
        sol_view.Sol_view()

        ## -----------------------------------------------
        ## --------- Settings view configuration ---------

        self.settings_panel = ui.UIAnchorLayout(size_hint=(1, 1))
        self.settings_panel.with_background(color=arcade.uicolor.GRAY_CONCRETE)
        content_anchor.add(self.settings_panel, anchor_x="left", anchor_y="top")
        settings_view.Settings_view(anchor=self.settings_panel)

        ## -----------------------------------------------
        ## --------- Default view configuration ----------

        self.game_panel.visible = True
        self.sol_panel.visible = False
        self.settings_panel.visible = False

        ## ----------------------------------------------------------------
        ## ---- Anchor and button configuration for in-game navigation ----
        
        box_for_navigation_buttons = ui.UIButtonRow(vertical=True, size_hint=(0.3, 0.9))
        box_for_navigation_buttons.with_padding(all=10)
        box_for_navigation_buttons.with_background(color=arcade.uicolor.WHITE_CLOUDS)
                        
        box_for_navigation_buttons.add_button("Game", style=ui.UIFlatButton.STYLE_BLUE, size_hint=(1, 0.1))
        box_for_navigation_buttons.add_button("Sol", style=ui.UIFlatButton.STYLE_BLUE, size_hint=(1, 0.1))
        box_for_navigation_buttons.add_button("Settings", style=ui.UIFlatButton.STYLE_BLUE, size_hint=(1, 0.1))
                               
        main_anchor.add(box_for_navigation_buttons, anchor_x="right", anchor_y="bottom")
                        
        @box_for_navigation_buttons.event("on_action")
        def on_action(event: ui.UIOnActionEvent):
            if event.action == "Game":
                self.game_panel.visible = True
                self.sol_panel.visible = False
                self.settings_panel.visible = False
            elif event.action == "Sol":
                self.game_panel.visible = False
                self.sol_panel.visible = True
                self.settings_panel.visible = False
            elif event.action == "Settings":
                self.game_panel.visible = False
                self.sol_panel.visible = False
                self.settings_panel.visible = True

        ## -----------------------------------------------
        ## ---- Adding everything to the main anchor -----

        self.ui_manager.add(main_anchor) ## addition at the very end of the achor containing everything

        ## -----------------------------------------------
        ## ------------- Cash display system -------------
        
        self.money = calculateMoney.Money()
        self.display_money = ui.UILabel(
            text="Money : 0",
            font_size=30
        )

        banner_anchor.add(self.display_money, anchor_x="center", anchor_y="center")

        ## -----------------------------------------------
        ## ---------------- System planet ----------------

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
        
        store_button_box = ui.UIBoxLayout(space_between=10)
        
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
        
        anchor_for_the_store_button_box = ui.UIAnchorLayout()
        anchor_for_the_store_button_box.add(
            child=store_button_box,
            anchor_x="left",
            anchor_y="center",
            align_x=20,
        )
        
        self.game_panel.add(anchor_for_the_store_button_box)


    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.sun.Click_to_update()

    def on_show_view(self):
        self.ui_manager.enable()

    def on_hide_view(self):
        self.ui_manager.disable()

    def on_draw(self):
        self.clear()
        self.display_money.text = f"money: {self.money.get_money():.2f}"
        self.planets.draw()
        self.ui_manager.draw()

        
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