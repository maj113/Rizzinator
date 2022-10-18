from random import uniform
from gameplay import mia
from time import sleep
from misc.gym import gymExcercise
from misc.plstats import player_stats
story_list = []
menuchoices = ("Hit the gym [1]\n ","Exit the game [2]\n"," Check current stats [3]\n"," Play story from beginning [4]\n"," Continue story [5]\n")

def slow_print(s, speed = 5):
    for c in s:
        print(c,end="")
        sleep(uniform(0.05, 0.2)*(1/speed))
    print()

def gamemenu():
    print("What do you want to do:\n\n " , *menuchoices,)
    gamechoice = input("Input the number next to the action you want to do ")
    
    if  gamechoice == "1":
        gymExcercise()
    
    elif gamechoice == "2":
        print("Aight go touch grass")
        exit()

    elif gamechoice == "3":
        print("Looks= ",player_stats[0],"Jacked= ",player_stats[0],"Attraction= ",player_stats[0])
        sleep(5)
        
    elif gamechoice == "4":
        def characterselector():
            global selected_story
            print("\nSelect your character")
            if mia.mialvl[0] <= player_stats[0] and mia.mialvl[1] <= player_stats[1] and mia.mialvl[2] <= player_stats[2]:
                print("\nyou can pick Mia")
            selected_story = input("\nWho are you picking? ")
            if (selected_story) == ("mia"):
                story_list.append(selected_story)
                mia.miaintro() 
            elif mia.mialvl[0] > player_stats[0] and mia.mialvl[1] >player_stats[1] and mia.mialvl[2] > player_stats[2]:
                print("You can not play Mia's story if your stats are too low!")
            else: gamemenu()
        characterselector()
    
    elif gamechoice == "5":
        def savestate():
            print(f"you can continue {story_list}'s story")
            savechoice1 = input("Which story do you want to continue? ")
            if savechoice1 not in story_list:
                menuchoice = input("You cannot continue this story, do you want to go back to the main menu? ")
                if menuchoice == "yes":
                    gamemenu()
                else: savestate()
            else:
                input("where do you want to continue?")
        savestate()
