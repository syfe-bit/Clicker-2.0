import arcade
import arcade.gui

class ShopButton(arcade.gui.UIFlatButton):
    def __init__(self, initial_price, unlock_amount=0, callback=None, **kwargs):
        self.price = initial_price
        self.unlock_amount = unlock_amount
        self.callback = callback

        super().__init__(
            text=f"Améliorer - {self.price}$",
            width=200, 
            height=60,
            **kwargs)

        if callback:
            self.on_click = callback

    def update_price(self, new_price):
        self.price = new_price
        self.text = f"Améliorer - {self.price:.2f}$"

    def set_available(self, available: bool):
        self.disabled = not available

    def update_visibility(self, argent_joueur):
        self.visible = argent_joueur >= self.unlock_amount