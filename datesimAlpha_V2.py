#Rizzsim Aplha release 2
#KrpanKodingKompany, All rights reserved 2022-2023
from time import sleep
from misc.PLStats import MoneyAmount, player_stats, playername, money
from gameplay.Mia import mialvl
from gameplay.Emma import emmalvl
import misc.MainMenu as mm 

#only using Mia for now since other dont have stories yet, not sure how this even scales with multiple. @gorchii wanna implement?
#woman_list = ["Mia", "Emma", "Lana", "Jane", "Jenny", "Anna", "Mimi", "Lina", "Anya"]

playername()
mm.slow_print("\nYour current stats are: \n", speed=4)
print("\n Looks = ",player_stats[0],"\n Jacked = ",player_stats[1],"\n Attraction = ",player_stats[2],"\n Money = ",money[0],"\n")
sleep(1)
if mialvl[0] <= player_stats[0] and mialvl[1] <= player_stats[1] and mialvl[2] <= player_stats[2]:
    mm.slow_print("you can pick Mia\n")
if emmalvl[0] <= player_stats[0] and emmalvl[1] <= player_stats[1] and emmalvl[2] <= player_stats[2]:
    mm.slow_print("you can pick Emma\n")
    mm.gamemenu()
else: 
    mm.slow_print("your stats are too low, you can get better stats in the menu.\n")
    mm.gamemenu()
sleep(5)




#Credits:
#Maj - Lead programmer
#Gorazd - Lead Writer, programmer, idea provider
