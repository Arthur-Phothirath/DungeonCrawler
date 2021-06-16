from dungeon.model.character import ClassicCharacter
import random


class ClassicMonster(ClassicCharacter):

    def __init__(self, name, life, mana, strenght, defense, intel, speed):
        super().__init__(name, life, mana, strenght, defense, intel, speed)

    def loot(self, sac):

        if ClassicMonster.get_health(self) == 0:
            sac.append("Coin")

    def sound(self):

        monster_sound = random.randint(0, 2)

        if monster_sound == 0:
            print("Grrrr...")
        elif monster_sound == 1:
            print("Le monstre prend un air menaçant.")
        else:
            print("Le monstre à l'air de vous craindre.")

    def loot(self, sac):
        print("Vous avez obtenu une potion! Vous avez actuellement dans votre sac: ")
        sac.append("potion")
