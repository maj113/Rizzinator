#random comment cause this is what devs do... right?
from time import sleep
from random import randint


def gymExcercise():
    from misc.mainmenu import gamemenu, slow_print
    from misc.plstats import player_stats
    slow_print("\nYou packed your gym shorts, protein shake and headed to your local gym.")
    print("\nYour current stats are: \n\n","Looks =",player_stats[0],"\n Jacked =",player_stats[1],"\n Attraction =",player_stats[2],"\n")
    excerciseTime = int(input("\nhow long do you wish to excercise for? Use seconds: "))
    if excerciseTime > 20:
        slow_print("\nyou can not excercise for more than 20 seconds!", speed=4)
        gymExcercise()
    else:
        player_stats[1] = player_stats[1] + excerciseTime
        for l in range(excerciseTime):
            print(" 💪", flush = True,end="")
            sleep(1)
        print()
        slow_print("\nyou got closer to being an absolute CHAD, good work chap. Your new stats are\n")
        print("Looks=",player_stats[0],"\n Jacked=",player_stats[1],"\n Attraction=",player_stats[2],"\n")
        gamemenu()
    
  

