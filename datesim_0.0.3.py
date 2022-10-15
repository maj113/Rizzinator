#Rizzsim_0.0.3
#KrpanKodingKompany, All rights reserved 2022
from stories import woman_intro as wi, MiaStories as ms
from time import sleep
from random import choice
import misc.mainmenu as mm
from misc.stats import player_stats
from gameplay import mia

#woman_list = ["Mia", "Emma", "Lana", "Jane", "Jenny", "Anna", "Mimi", "Lina", "Anya"]
woman_list = ["Mia"]
player = input(str("what is your name? "))
print("Your current stats are: \n","Looks=",player_stats[0],"\n Jacked=",player_stats[1],"\n Attraction=",player_stats[2])
sleep(2)
mia.levelneeded()
if mia.mialvl[0:2] < player_stats[0:2]:
    print("you can pick Mia")
    sleep(2)
    mm.gamemenu()
else: 
    print("your stats are too low, you can get better stats in the gamemenu")
    sleep(2)
    mm.gamemenu()
sleep(5)






#I like tall goth futas hihi
"""
Credits:
Maj - Lead programmer, spell checker
Gorazd - Lead Writer, code review, idea provider
"""