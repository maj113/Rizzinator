#Rizzsim_0.0.3
#KrpanKodingKompany, All rights reserved 2022
from stories import woman_intro as wi, MiaStories as ms
from time import sleep
from random import choice
import misc.mainmenu as mm
from misc.stats import player_stats
#woman_list = ["Mia", "Emma", "Lana", "Jane", "Jenny", "Anna", "Mimi", "Lina", "Anya"]
woman_list = ["Mia"]
woman = (choice(woman_list))
player = input(str("what is your name? "))
print("Your current stats are: \n","Looks=",player_stats[0],"\n Jacked=",player_stats[1],"\n Attraction=",player_stats[2])
sleep(5)
def interactions():
    if (woman == "Mia"):
        if player_stats >= [20,25,2]: 
            print(wi.miaIntr)
            sleep(0)
            accept_mia = input("do you wish to continue Mia's story? If so, type yes ")
            if (accept_mia == "yes" or "y"):
                print(ms.MiaStory1)
                sleep(0)
                mm.gamemenu()
            else: interactions()
        else: interactions() 
interactions()




#I like tall goth futas
"""
Credits:
Maj - Lead programmer, spell checker
Gorazd - Lead Writer, code review, idea provider
"""