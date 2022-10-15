from random import randint
from time import sleep
from misc.stats import stats1
stats1()
from misc.stats import player_stats
menuchoices = ("Hit the gym [1]\n ", "Exit the game [2]\n", " Check current stats [3]" )
def gamemenu():
    print("What do you want to do:\n " , *menuchoices)
    gamechoice = input("Input the number next to the action you want to do ")
    if  gamechoice == "1":
        player_stats[1] = (player_stats[1]+randint(0,2))
    elif gamechoice == "2":
        print("Aight go touch grass")
        exit()
    elif gamechoice == "3":
        print("Looks= ",player_stats[0],"Jacked= ",player_stats[0],"Attraction= ",player_stats[0])
        sleep(5)
