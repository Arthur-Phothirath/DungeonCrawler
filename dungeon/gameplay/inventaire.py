
def open_sac(sac):
    choix = input("Votre sac contient: ", sac, ". Voulez-vous utiliser une potion? : Y/N")
    if choix == "Y" or choix == "y":
        sac.remove("potion")
        print(sac)
    elif choix == "N" or choix == "n":
        return
