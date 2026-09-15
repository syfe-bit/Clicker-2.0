class Upgrade:
    def __init__(self, initial_price: float):
        self.price = initial_price
        self.nb_of_times_purchased_upgrade = 0
        self.STATIC_SPEED_EFFECT = 1.1
        self.STATIC_MONEY_MULTIPLIER_EFFECT = 1.1
        self.speed_effect = 0
        self.money_multiplier_effect = 0

    def add_nb_of_times_purchased_upgrade(self):
        self.nb_of_times_purchased_upgrade += 1

    def add_effect(self):
        self.speed_effect = self.STATIC_SPEED_EFFECT ** self.nb_of_times_purchased_upgrade
        self.money_multiplier_effect = self.STATIC_MONEY_MULTIPLIER_EFFECT ** self.nb_of_times_purchased_upgrade

    def get_effect(self):
        return self.speed_effect, self.money_multiplier_effect