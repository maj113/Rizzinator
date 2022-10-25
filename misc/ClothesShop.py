#so good looking much suit and pants
from time import sleep



def clothesShoping():
    from misc.PLStats import player_stats, PlayerName
    from misc.MainMenu import slow_print, gamemenu
    slow_print("\n\"A real man needs a good looking outfit\" you think to yourself while walking to the local red cross to pick out some serious drip. \"Hello! how can I help you? The red cross employee asks you.",speed=7)
    sleep(1)
    interactionChoice = int(input("\nI would like to acquire some drip m'lady [1]\n" "WHAT ARE YOU DOIN IN MY SWAMP!?!? [2] \n"))
    print("\033[A                             \033[A")
    if interactionChoice == 1:
        pickingClothes()

    elif interactionChoice == 2:
        slow_print("\n\"GUARDS!!!\" shouts the cashier. Three huge men with sunglasses and black suits escort you from the building.")
        sleep(1)
        gamemenu()

    else:
        slow_print("STOP DEFYING THE GAMES ORDERS YOU- ENOUGH! TO THE MENU WITH YOU!!!")
        gamemenu()


def pickingClothes():
    from misc.MainMenu import slow_print, gamemenu
    from misc.PLStats import player_stats, PlayerName
    slow_print("\nUmmm... o-kayy? What kind of \"drip\" are you looking for? These are the outfits. Cuggi leather jacket Suit DasAdi sweater and fanny pack Lidl outfit")
    selectedDrip = int(input("Input the the number of the clothing item you wish to select?").strip())
    if selectedDrip == 1:
        sleep(1)
        slow_print("\"Daaayumm this jacket makes me look great\"")
        player_stats[0] = player_stats[0] + 10
        gamemenu()
    elif selectedDrip == 2:
        sleep(1)
        slow_print("\"I look classy!\"")
        player_stats[0] = player_stats[0] + 15
        gamemenu()
    elif selectedDrip == 3:
        sleep(1)
        slow_print("\"I look like a drug dealer!\"")
        player_stats[0] = player_stats[0] + 7
        gamemenu()
    elif selectedDrip == 4:
        sleep(1)
        slow_print(f"You put on the Lidl outfit, and feel a surge of pure god-like energy coursing through your veins. You hear a booming voice \"{PlayerName} I KNEW YOU WERE THE CHOSEN ONE! GO GET 'EM TIGER!\"")
        player_stats[0] = player_stats[0] + 25
        gamemenu()
    else: 
        slow_print("STOP DEFYING THE GAMES ORDERS YOU- ENOUGH! TO THE MENU WITH YOU!!!")
        gamemenu()


