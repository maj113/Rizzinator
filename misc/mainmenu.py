from random import randint
from gameplay import mia
from time import sleep
from misc.gym import gymExcercise
from misc.stats import stats1

stats1()
from misc.stats import player_stats
menuchoices = ("Hit the gym [1]\n ", "Exit the game [2]\n", "Check current stats [3]\n"," Play story from beginning [4]")
def gamemenu():
    print("What do you want to do:\n " , *menuchoices)
    gamechoice = input("Input the number next to the action you want to do ")
    if  gamechoice == "1":
        player_stats[1] = (player_stats[1]+randint(0,2))
        gymExcercise()
    
    elif gamechoice == "2":
        print("Aight go touch grass")
        exit()

    elif gamechoice == "3":
        print("Looks= ",player_stats[0],"Jacked= ",player_stats[0],"Attraction= ",player_stats[0])
        sleep(5)
        
    elif gamechoice == "4":
        print("Select your character")
        if mia.levelneeded() < player_stats:
            print("you can pick Mia")
        selected_story = input("Who are you picking? ")
        print(selected_story)
        if (selected_story) == ("mia"):
            mia.miaintro()

        elif player_stats < mia.mialvl:
            print("You can not play Mia's story if your stats are too low!")
        else: exit()