import arcade

class Planet(arcade.Sprite):
    def __init__(self, x: float, y: float, orbit_speed: float, rotation_angle: float, money, money_value: float, nb_of_times_purchased_upgrade):
        image_sprite = f"sprites/planet/{self.__class__.__name__.lower()}.png"
        super().__init__(image_sprite, scale=1)
        self.center_x = x
        self.center_y = y
        self.nb_of_times_purchased_upgrade = nb_of_times_purchased_upgrade
        self.automation = False
        self.money = money
        self.money_value = money_value
        self.money_effect = 1
        self.ORBIT_SPEED = orbit_speed
        self.orbit_speed = orbit_speed
        self.total_angle = 0
        self.rotation_angle = rotation_angle
        windows = arcade.get_window()
        self.window_width = windows.width //2
        self.window_height = windows.height //2

    def apply_automation(self):
        self.automation = self.nb_of_times_purchased_upgrade.nb_of_times_purchased_upgrade >= 1

    def apply_effect_speed(self, effect: float):
        self.orbit_speed = self.ORBIT_SPEED * effect

    def apply_effect_money(self, effect: float):
        self.money_effect = effect
        
    def update(self, delta_time):
        if self.automation:
            self.alpha = 255
            ## ------------------------------------------
            ## This allows the planet to orbit the Sun.
            x_position, y_position = arcade.math.rotate_point(self.center_x, self.center_y, self.window_width, self.window_height, self.orbit_speed)
            self.center_x = x_position
            self.center_y = y_position
            self.total_angle += self.orbit_speed
            if self.total_angle == 360:
                self.money.add_money(self.money_value, self.money_effect)
                self.total_angle = 0
            ## ------------------------------------------
            self.angle += self.rotation_angle ## It causes the planet to rotate on its axis, not to orbit the sun.
        else:
            self.alpha = 0