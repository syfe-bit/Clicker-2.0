class Money:
    def __init__(self):
        self.money = 0

    def add_money(self):
        self.money += 10

    def withdraw_money(self, price_item):
        if self.money >= price_item:
            self.money -= price_item
            return True

        return False

    def get_money(self):
        return self.money