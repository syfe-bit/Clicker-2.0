import arcade

class Planet(arcade.Sprite):
    def __init__(self, image_sprite, scale=1.0, x=0, y=0, orbit_speed=1, rotation_angle=1):
        super().__init__(image_sprite, scale)
        self.center_x = x
        self.center_y = y
        self.orbit_speed = orbit_speed
        self.rotation_angle = rotation_angle
        windows = arcade.get_window()
        self.window_width = windows.width //2
        self.window_height = windows.height //2
        

    def update(self, delta_time):
        x_position, y_position = arcade.math.rotate_point(self.center_x, self.center_y, self.window_width, self.window_height, self.orbit_speed)
        self.center_x = x_position
        self.center_y = y_position
        self.angle += self.rotation_angle 


class Sun(Planet):
    def __init__(self, x, y, orbit_speed, rotation_angle):
        super().__init__("sprites/planet/sun.png", scale=1, x=x, y=y, orbit_speed=orbit_speed, rotation_angle=rotation_angle)
        
class Mercury(Planet):
    def __init__(self, x, y, orbit_speed, rotation_angle ):
        super().__init__("sprites/planet/mercury.png", scale=1, x=x, y=y, orbit_speed=orbit_speed, rotation_angle=rotation_angle)

class Venus(Planet):
    def __init__(self, x, y, orbit_speed, rotation_angle ):
        super().__init__("sprites/planet/sun.png", scale=1, x=x, y=y, orbit_speed=orbit_speed, rotation_angle=rotation_angle)

class Earth(Planet):
    def __init__(self, x, y, orbit_speed, rotation_angle ):
        super().__init__("sprites/planet/sun.png", scale=1, x=x, y=y, orbit_speed=orbit_speed, rotation_angle=rotation_angle)

class Mars(Planet):
    def __init__(self, x, y, orbit_speed, rotation_angle ):
        super().__init__("sprites/planet/sun.png", scale=1, x=x, y=y, orbit_speed=orbit_speed, rotation_angle=rotation_angle)

class Jupiter(Planet):
    def __init__(self, x, y, orbit_speed, rotation_angle ):
        super().__init__("sprites/planet/sun.png", scale=1, x=x, y=y, orbit_speed=orbit_speed, rotation_angle=rotation_angle)

class Saturn(Planet):
    def __init__(self, x, y, orbit_speed, rotation_angle ):
        super().__init__("sprites/planet/sun.png", scale=1, x=x, y=y, orbit_speed=orbit_speed, rotation_angle=rotation_angle)

class Uranus(Planet):
    def __init__(self, x, y, orbit_speed, rotation_angle ):
        super().__init__("sprites/planet/sun.png", scale=1, x=x, y=y, orbit_speed=orbit_speed, rotation_angle=rotation_angle)

class Neptune(Planet):
    def __init__(self, x, y, orbit_speed, rotation_angle ):
        super().__init__("sprites/planet/sun.png", scale=1, x=x, y=y, orbit_speed=orbit_speed, rotation_angle=rotation_angle)