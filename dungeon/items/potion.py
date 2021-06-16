
class Potion:
    def __init__(self, name, heal):
        self.name = name
        self.heal = heal

    def get_name(self):
        return self.name

    def get_healing_value(self):
        return self.heal

    def healing(self, player):
        player.life = self.heal + player.life
        print("Vous vous êtes soignez de", Potion.get_healing_value(self), ".", "Vous êtes à", player.get_health(), "pv")


potion = Potion("potion simple", 10)

