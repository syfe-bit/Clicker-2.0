import arcade

class Planet(arcade.Sprite):
    def __init__(self, x, y, orbit_speed, rotation_angle, money, money_value):
        image_sprite = f"sprites/planet/{self.__class__.__name__.lower()}.png"
        super().__init__(image_sprite, scale=1)
        self.starting_point_x = x
        self.starting_point_y = y
        self.center_x = x
        self.center_y = y
        self.money = money
        self.money_value = money_value
        self.money_effect = 1
        self.orbit_speed = orbit_speed
        self.total_angle = 0
        self.ROTATION_ANGLE = rotation_angle
        self.rotation_angle = rotation_angle
        windows = arcade.get_window()
        self.window_width = windows.width //2
        self.window_height = windows.height //2

    def apply_effect_speed(self, effect: float):
        self.rotation_angle = self.ROTATION_ANGLE * effect

    def apply_effect_money(self, effect: float):
        self.money_effect = effect
        
    def update(self, delta_time):
        
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