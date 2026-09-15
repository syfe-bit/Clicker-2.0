class Money:
    def __init__(self):
        self.money = 0

    def add_money(self, money_value: float, money_multiplier_effect: float):
        self.money += money_value * money_multiplier_effect

    def withdraw_money(self, price_item: float=1):
        if self.money >= price_item:
            self.money -= price_item
            return True

        return False

    def get_money(self):
        return self.money