
def choice_gameplay(player, monster, sac):

    while monster.get_health() > 0:
        if player.get_health() > 0:
            choice = input("1: Attack 2: Fuire: ")

            if choice == "1":
                print("Vous portez une attaque au", monster.get_name())
                player.attack_target(monster)
                print("Il lui reste: ", monster.get_health(), "pv")
                if monster.get_health() > 0:
                    print("Le monstre vous attaque!")
                    monster.attack_target(player)
                    if player.get_defense() > 0:
                        print("Le monstre vous a enlevé ", monster.get_strenght()-player.get_defense(), "pv .Il vous reste ",
                              player.get_health(), "pv")
                    else:
                        print("Le monstre vous a enlevé ", monster.get_strenght(), "pv .Il vous reste ", player.get_health(), "pv")
                else:
                    print("Vous avez vaincus le monstre!")
                    monster.loot(sac)
                    print(sac)
                    break
            elif choice == "2":
                print("Vous fuyez!")
                break
        else:
            print("Vous avez succombé à vos blessures. GAME OVER")
            break
