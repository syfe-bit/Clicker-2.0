import arcade
from PIL import ImageDraw, Image

class Planet(arcade.Sprite):
    def __init__(self, x, y, orbit_speed, rotation_angle, money):
        image_sprite = f"sprites/planet/{self.__class__.__name__.lower()}.png"
        super().__init__(image_sprite, scale=1)
        self.center_x = x
        self.center_y = y
        self.money = money
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
    def __init__(self, x, y, orbit_speed, rotation_angle, money, steps=60):
        super().__init__(x, y, orbit_speed, rotation_angle, money)
        image_path = f"sprites/planet/{self.__class__.__name__.lower()}.png"
        self.progress = 0
        self.steps = steps
        self.frames = self._generate_frames(image_path, steps)
        self.texture = self.frames[0]  # commence invisible (0% rempli)
        self.automation = False

    def _generate_frames(self, image_path, steps):
        base = Image.open(image_path).convert("RGBA")
        w, h = base.size
        cx, cy = w / 2, h / 2
        r = (w**2 + h**2) ** 0.5

        frames = []
        for i in range(steps + 1):
            angle = 360 * i / steps

            mask = Image.new("L", (w, h), 0)
            draw = ImageDraw.Draw(mask)
            draw.pieslice(
                [cx - r, cy - r, cx + r, cy + r],
                start=-90, end=angle - 90,
                fill=255
            )

            frame = base.copy()
            _, _, _, alpha = frame.split()
            new_alpha = Image.composite(alpha, Image.new("L", (w, h), 0), mask)
            frame.putalpha(new_alpha)

            frames.append(arcade.Texture(image=frame))

        return frames

    def Click_to_update(self):
        if self.progress < 100:
            self.progress += 30 

        if self.progress >= 100:
            self.money.add_money()
            self.progress -= 100
                            
        index = int((self.progress / 100) * self.steps)
        self.texture = self.frames[index]

    def update(self, delta_time):
        self.angle += self.rotation_angle  # tourne sur lui-même, pas d'orbite

        if self.automation:
            if self.progress < 100:
                self.progress += 30 
                if self.progress > 100:
                    self.progress -= 100
            else:
                self.progress -= 100

            index = int((self.progress / 100) * self.steps)
            self.texture = self.frames[index]
        
class Mercury(Planet):
    pass

class Venus(Planet):
    pass

class Earth(Planet):
    pass

class Mars(Planet):
    pass

class Jupiter(Planet):
    pass

class Saturn(Planet):
    pass

class Uranus(Planet):
    pass

class Neptune(Planet):
    pass