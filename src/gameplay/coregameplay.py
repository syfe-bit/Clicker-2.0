import arcade
from PIL import Image, ImageDraw

class Planet(arcade.Sprite):
    def __init__(self, image_sprite, scale=1.0, x=0, y=0, steps=60):
        super().__init__(image_sprite, scale)
        self.center_x = x
        self.center_y = y
        self.progress = 0
        self.fill_speed = 2
        self.steps = steps
        self.frames = self._generate_frames(image_sprite, steps)

    def update(self, delta_time):
        if self.progress < 360:
            self.progress += self.fill_speed * delta_time
            if self.progress > 360:
                self.progress = 360
        else:
            self.progress -= 360

class Sun(Planet):
    def __init__(self, x, y):
        super().__init__("sprites/planet/sun.png", scale=1, x=x, y=y)

    def _generate_frames(self, image_path, steps):
            base = Image.open(image_path).convert("RGBA")
            w, h = base.size
            cx, cy = w / 2, h / 2
            # rayon assez grand pour couvrir toute l'image, même en diagonale
            r = (w**2 + h**2) ** 0.5
    
            frames = []
            for i in range(steps + 1):
                angle = 360 * i / steps
    
                # masque noir = caché, blanc = visible
                mask = Image.new("L", (w, h), 0)
                draw = ImageDraw.Draw(mask)
                # PIL compte les angles depuis l'axe horizontal (3h), sens horaire
                # -90 = départ en haut
                draw.pieslice(
                    [cx - r, cy - r, cx + r, cy + r],
                    start=-90, end=angle - 90,
                    fill=255
                )
    
                frame = base.copy()
                # on combine le masque avec la transparence déjà existante
                r_ch, g_ch, b_ch, a_ch = frame.split()
                new_alpha = Image.composite(a_ch, Image.new("L", (w, h), 0), mask)
                frame.putalpha(new_alpha)
    
                frames.append(arcade.Texture(image=frame))
    
            return frames
    
    def update(self, delta_time):
        if self.progress < 360:
            self.progress += self.fill_speed * delta_time
            if self.progress > 360:
                self.progress = 360
        else:
            self.progress -= 360
    
        index = int((self.progress / 360) * self.steps)
        self.texture = self.frames[index]

class Mercury(Planet):
    def __init__(self, x, y):
        super().__init__("sprites/planet/mercury.png", scale=1, x=x, y=y)

class Venus(Planet):
    def __init__(self, x, y):
        super().__init__("sprites/planet/sun.png", scale=1, x=x, y=y)

class Earth(Planet):
    def __init__(self, x, y):
        super().__init__("sprites/planet/sun.png", scale=1, x=x, y=y)

class Mars(Planet):
    def __init__(self, x, y):
        super().__init__("sprites/planet/sun.png", scale=1, x=x, y=y)

class Jupiter(Planet):
    def __init__(self, x, y):
        super().__init__("sprites/planet/sun.png", scale=1, x=x, y=y)

class Saturn(Planet):
    def __init__(self, x, y):
        super().__init__("sprites/planet/sun.png", scale=1, x=x, y=y)

class Uranus(Planet):
    def __init__(self, x, y):
        super().__init__("sprites/planet/sun.png", scale=1, x=x, y=y)

class Neptune(Planet):
    def __init__(self, x, y):
        super().__init__("sprites/planet/sun.png", scale=1, x=x, y=y)