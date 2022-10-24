#so good looking much suit and pants
from time import sleep
from misc.MainMenu import slow_print, gamemenu
from misc.PLStats import player_stats

def pickingClothes():
    slow_print("Ummm... o-kayy? What kind of \"drip\" are you looking for? These are the outfits. \"Cuggi leather jacket", "Suit", "DasAdi sweater and fanny pack", "Lidl outfit\"")
    selectedDrip = int(input("Input the the number of the clothing item you wish to select?").strip())
    if selectedDrip == 1:
        sleep(1)
        slow_print("\"Daaayumm this jacket makes me look great\"")
        player_stats[0] = player_stats[0] + 10
    elif selectedDrip == 2:
        sleep(1)
        slow_print("\"I look classy!\"")
        player_stats[0] = player_stats[0] + 15
    elif selectedDrip == 3:
        sleep(1)
        slow_print("\"I look like a drug dealer!\"")
        player_stats[0] = player_stats[0] + 7
    elif selectedDrip == 4:
        sleep(1)
        slow_print(f"You put on the Lidl outfit, and feel a surge of pure god-like energy coursing through your veins. You hear a booming voice \"{PlayerName} I KNEW YOU WERE THE CHOSEN ONE! GO GET 'EM TIGER!\"")
        player_stats[0] = player_stats[0] + 25
    else: 
        slow_print("STOP DEFYING THE GAMES ORDERS YOU- ENOUGH! TO THE MENU WITH YOU!!!")
        gamemenu()

def clothesShoping():
    slow_print("\n\"A real man needs a good looking outfit\" you think to yourself while walking to the local red cross to pick out some serious drip. \Hello! how can I help you? The red cross employee asks you.")
    sleep(1)
    interactionChoice = int(input("\n input 1 to say \"I would like to acquire some drip m'lady\" or 2, to say \"WHAT ARE YOU DOIN IN MY SWAMP!?!?\""))
   
    if interactionChoice == 1:
        pickingClothes()

    elif interactionChoice == 2:
        slow_print("\n\"GUARDS!!!\" shouts the cashier. Three huge men with sunglasses and black suits escort you from the building.")
        sleep(1)
        gamemenu()

    else:
        slow_print("STOP DEFYING THE GAMES ORDERS YOU- ENOUGH! TO THE MENU WITH YOU!!!")
        gamemenu()
