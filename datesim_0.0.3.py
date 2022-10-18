#Rizzsim Aplha release 1
#KrpanKodingKompany, All rights reserved 2022
from stories import woman_intro as wi, MiaStories as ms
from time import sleep
from random import choice
from gameplay import mia
import misc.mainmenu as mm
from misc.plstats import player_stats
#woman_list = ["Mia", "Emma", "Lana", "Jane", "Jenny", "Anna", "Mimi", "Lina", "Anya"]
player = input(str("what is your name? "))
print("\nYour current stats are: \n\n","Looks=",player_stats[0],"\n Jacked=",player_stats[1],"\n Attraction=",player_stats[2],"\n")
sleep(2)
mia.levelneeded()
if mia.mialvl[0] <= player_stats[0] and mia.mialvl[1] <= player_stats[1] and mia.mialvl[2] <= player_stats[2]:
    print("you can pick Mia")
    sleep(2)
    mm.gamemenu()
else: 
    print("your stats are too low, you can get better stats in the menu.")
    sleep(2)
    mm.gamemenu()
sleep(5)




"""
Credits:
Maj - Lead programmer
Gorazd - Lead Writer, programmer, idea provider
"""