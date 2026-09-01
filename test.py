import arcade

class MonJeu(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Test Sprite")
        self.perso = arcade.Sprite("sprites/planet/sun.png", scale=1)
        self.perso.center_x = 400
        self.perso.center_y = 300

        # On crée une liste de sprites et on y ajoute notre perso
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self.perso)

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()  # on dessine la liste, pas le sprite seul

    def on_update(self, delta_time):
        self.perso.center_x += 1

MonJeu()
arcade.run()