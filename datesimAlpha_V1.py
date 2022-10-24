#Rizzsim Aplha release 1
#KrpanKodingKompany, All rights reserved 2022
from time import sleep
from tokenize import maybe
from gameplay.Mia import mialvl
import misc.MainMenu as mm 
from misc.PLStats import player_stats, playername
#only using Mia for now since other dont have stories yet, not sure how this even scales with multiple. @gorchii wanna implement?
#woman_list = ["Mia", "Emma", "Lana", "Jane", "Jenny", "Anna", "Mimi", "Lina", "Anya"]
playername()
mm.slow_print("\nYour current stats are: \n", speed=4)
print("Looks =",player_stats[0],"\nJacked =",player_stats[1],"\nAttraction =",player_stats[2],"\n")
sleep(1)
if mialvl[0] <= player_stats[0] and mialvl[1] <= player_stats[1] and mialvl[2] <= player_stats[2]:
    mm.slow_print("you can pick Mia\n")
    mm.gamemenu()
else: 
    mm.slow_print("your stats are too low, you can get better stats in the menu.\n")
    mm.gamemenu()
sleep(5)




#Credits:
#Maj - Lead programmer
#Gorazd - Lead Writer, programmer, idea provider
