from dungeon.room import random_room
from dungeon.model.character import ClassicCharacter


sac = ["Epée"]
player1 = ClassicCharacter("Warrior", 20, 20, 20, 10, 20, 20)


def intro(player, sac, difficulty):

    startgame = input("Vous vous approchez du donjon. Voulez-vous rentrez dans le donjon? (O/N) ")

    if startgame == "n" or startgame == "N":
        print("Peut-être pour une prochaine fois.")
        return
    elif startgame == "o" or startgame == "O":
        print("Bienvenu dans le donjon.")
        random_room(player, sac, difficulty)


intro(player1, sac, 3)
