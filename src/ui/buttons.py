import arcade
import arcade.gui

class ShopButton(arcade.gui.UIFlatButton):
    def __init__(self, initial_price: float, number_of_upgrades_to_from_the_previous_planet, number_of_upgrades_to_unlock: float =0,callback=None, **kwargs):
        self.price = initial_price
        self.number_of_upgrades_to_from_the_previous_planet = number_of_upgrades_to_from_the_previous_planet
        self.number_of_upgrades_to_unlock = number_of_upgrades_to_unlock
        self.callback = callback

        super().__init__(
            text=f"Améliorer - {self.price}$",
            width=200, 
            height=60,
            **kwargs)

        if callback:
            self.on_click = callback

    def update_price(self, new_price: float):
        self.price = new_price
        self.text = f"Améliorer - {self.price:.2f}$"

    def update_visibility(self):

        if self.number_of_upgrades_to_from_the_previous_planet is None:
            unlocked  = True
        else:
            unlocked  = self.number_of_upgrades_to_from_the_previous_planet.nb_of_times_purchased_upgrade >= self.number_of_upgrades_to_unlock

        self.visible = unlocked
        self.disabled = not unlocked