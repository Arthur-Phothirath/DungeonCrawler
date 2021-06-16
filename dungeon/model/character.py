
class ClassicCharacter:
    def __init__(self, name, life, mana, strenght, defense, intel, speed):
        self.name = name
        self.life = life
        self.mana = mana
        self.strenght = strenght
        self.defense = defense
        self.intel = intel
        self.speed = speed

    def get_name(self):
        return self.name

    def get_health(self):
        return self.life

    def get_mana(self):
        return self.mana

    def get_strenght(self):
        return self.strenght

    def get_defense(self):
        return self.defense

    def get_intel(self):
        return self.intel

    def get_speed(self):
        return self.speed

    def damage(self, damage):
        if self.defense >= damage:
            self.life = self.life - 0
        else:
            self.life = self.life + (self.defense - damage)

    def attack_target(self, target):
        target.damage(self.strenght)
        if target.get_health == 0:
            print(target.get_name, "est mort.")
