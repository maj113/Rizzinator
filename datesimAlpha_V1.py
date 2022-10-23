#Rizzsim Aplha release 1
#KrpanKodingKompany, All rights reserved 2022
from stories import WomanIntro as wi, MiaStories as ms
from time import sleep
from gameplay import Mia
import misc.MainMenu as mm 
from misc.PLStats import player_stats, playername
#woman_list = ["Mia", "Emma", "Lana", "Jane", "Jenny", "Anna", "Mimi", "Lina", "Anya"]
playername()
mm.slow_print("\nYour current stats are: \n", speed=4)
print("Looks =",player_stats[0],"\nJacked =",player_stats[1],"\nAttraction =",player_stats[2],"\n")
sleep(0.5)
Mia.levelneeded()
if Mia.mialvl[0] <= player_stats[0] and Mia.mialvl[1] <= player_stats[1] and Mia.mialvl[2] <= player_stats[2]:
    mm.slow_print("you can pick Mia\n")
    mm.gamemenu()
else: 
    mm.slow_print("your stats are too low, you can get better stats in the menu.\n")
    mm.gamemenu()
sleep(5)




"""
Credits:
Maj - Lead programmer
Gorazd - Lead Writer, programmer, idea provider
"""