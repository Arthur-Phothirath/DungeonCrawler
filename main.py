
from dungeon.model.character import ClassicCharacter
from dungeon.modelmonster.monster import ClassicMonster
from dungeon import intro

sac = ["Epée"]
player1 = ClassicCharacter("Warrior", 20, 20, 20, 10, 20, 20)
monster1 = ClassicMonster("Goblin", 10, 10, 5, 0, 10, 10)

intro(player1, monster1, sac, 3)
