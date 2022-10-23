import imp
from random import uniform
from gameplay import Mia
from time import sleep
from misc.Gym import gymExcercise
from misc.PLStats import player_stats, stats1
from misc.PerfumeShop import goingToShop
story_list = []
menuchoices = ("  Play story from beginning [1]\n"," Continue story [2]\n"," Increase stats [3]\n ","Check current stats [4]\n"," Exit the game [5]\n")
statsmenu = ["  Hit the gym [1]\n"," Buy perfume [2]\n"," Go back [3]\n"]

def statsincreasemenu():
    slow_print("What do you want to do:\n " , speed=4)
    print(*statsmenu)
    slow_print("Input the number next to the action you want to do ",speed=5)
    statschoice = input().lower().strip()

    if statschoice == "1":
        gymExcercise()
    
    elif statschoice == "2":
        goingToShop()
    
    elif statschoice == "3": 
        gamemenu()

def slow_print(s, speed = 5):
    for c in s:
        print(c, end="", flush = True)
        sleep(uniform(0.1,0.25)*(1/speed))
    sleep(0.5)
    print()

def gamemenu():
    
    slow_print("What do you want to do:\n " , speed=4)
    print(*menuchoices)
    slow_print("Input the number next to the action you want to do ",speed=6)
    gamechoice = input().lower().strip()
    
    if  gamechoice == "3":
        statsincreasemenu()
    
    elif gamechoice == "5":
        slow_print("Aight go touch grass\n", speed=4)
        exit()

    elif gamechoice == "4":
        print("Looks =",player_stats[0],"\nJacked =",player_stats[1],"\nAttraction =",player_stats[2],"\n")
        sleep(1.5)
        gamemenu()
       
        
    elif gamechoice == "1":
        def characterselector():
            global story_list
            global selected_story
            slow_print("\nSelect your character", speed=4)
            if Mia.mialvl[0] <= player_stats[0] and Mia.mialvl[1] <= player_stats[1] and Mia.mialvl[2] <= player_stats[2]:
                slow_print("\nyou can pick Mia", speed=4)
            selected_story = input("\nWho are you picking? ").lower().strip()
            if (selected_story) == ("mia"):
                story_list = selected_story
                print(story_list)
                Mia.miaintro() 
            elif Mia.mialvl[0] > player_stats[0] and Mia.mialvl[1] >player_stats[1] and Mia.mialvl[2] > player_stats[2]:
                slow_print("You can not play Mia's story if your stats are too low!", speed=4)
            else: gamemenu()
        characterselector()
    
    elif gamechoice == "2":
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
    else: 
        slow_print("Thats not an option", speed=4)
        gamemenu()
