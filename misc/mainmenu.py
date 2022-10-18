from random import uniform
from gameplay import mia
from time import sleep
from misc.gym import gymExcercise
from misc.plstats import player_stats
story_list = []
menuchoices = ("Play story from beginning [1]\n"," Continue story [2]\n"," Hit the gym [3]\n ","Check current stats [4]\n"," Exit the game [5]\n")

def slow_print(s, speed = 5):
    for c in s:
        print(c, end="", flush = True)
        sleep(uniform(0.1,0.25)*(1/speed))
    sleep(0.5)
    print()

def gamemenu():
    
    print("What do you want to do:\n\n " , *menuchoices,)
   
    gamechoice = input("Input the number next to the action you want to do ")
    
    if  gamechoice == "3":
        gymExcercise()
    
    elif gamechoice == "5":
        print("Aight go touch grass")
        exit()

    elif gamechoice == "4":
        print("Looks= ",player_stats[0],"Jacked= ",player_stats[0],"Attraction= ",player_stats[0])
        sleep(5)
        
    elif gamechoice == "1":
        def characterselector():
            global story_list
            global selected_story
            print("\nSelect your character")
            if mia.mialvl[0] <= player_stats[0] and mia.mialvl[1] <= player_stats[1] and mia.mialvl[2] <= player_stats[2]:
                print("\nyou can pick Mia")
            selected_story = input("\nWho are you picking? ").lower().strip()
            if (selected_story) == ("mia"):
                story_list = selected_story
                print(story_list)
                mia.miaintro() 
            elif mia.mialvl[0] > player_stats[0] and mia.mialvl[1] >player_stats[1] and mia.mialvl[2] > player_stats[2]:
                print("You can not play Mia's story if your stats are too low!")
            else: gamemenu()
        characterselector()
    
    elif gamechoice == "2":
        def savestate():
            print(story_list)
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
