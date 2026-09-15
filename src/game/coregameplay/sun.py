import arcade
from PIL import ImageDraw, Image

import src.game.coregameplay.coregameplay as coregameplay

class Sun(coregameplay.Planet):
    def __init__(self, x, y, orbit_speed, rotation_angle, money, money_value, steps=60):
        super().__init__(x, y, orbit_speed, rotation_angle, money, money_value)
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
            self.money.add_money(self.money_value, self.money_effect)
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