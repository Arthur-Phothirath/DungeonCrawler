import random
from dungeon.gameplay.fight import choice_gameplay
from dungeon.modelmonster.monster import ClassicMonster

def random_room(player, sac, difficulty):

    print("Vous êtes anxieux à l'entrée du donjon.")
    room_number = 0
    difficulty = int(difficulty)
    while room_number < difficulty:
        value = random.randint(0, 4)

        print("Vous voyez la porte. Vous entrez...")

        if value == 0:
            EmptyRoom(player, sac)
        elif value == 1:
            ChestRoom(sac)
        elif value == 2 or value == 3:
            MonsterRoom(player, monster_selector(), sac)
        room_number = room_number + 1
        print("Répétition n :", room_number)
        print("La salle n: ", value)
        input()

def ChestRoom(sac):

    print("Vous voyez un coffre rutilant dans un recoin de la pièce... Vous trouvez un Coin.")
    sac.append("Coin")
    print(sac)

def MonsterRoom(player, monster, sac):
    print("Vous entendez des grnognements... Le monstre est proche...")
    print("C'est un", monster.get_name())
    choice_gameplay(player, monster, sac)

def EmptyRoom(player, sac):

    print("Vous scrutez chaque recoin de la salle...")
    if player.get_intel() >= 20:
        print("En fouillant bien vous trouvez quelquechose.")
        sac.append("Coin")
        print(sac)
    else:
        print("Vous ne trouvez rien.")

def monster_selector():
    monster_random = random.randint(0, 2)

    if monster_random == 0:
        monster_choice = ClassicMonster("Goblin", 5, 5, 5, 5, 5, 5)
    elif monster_random == 1:
        monster_choice = ClassicMonster("Hobgoblin", 10, 5, 10, 10, 5, 5)
    else:
        monster_choice = ClassicMonster("Lordgoblin", 20, 5, 10, 10, 10, 10)
    return monster_choice
