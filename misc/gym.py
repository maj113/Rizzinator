#random comment cause this is what devs do... right?
from time import sleep
from random import randint




def gymExcercise():
    from misc.mainmenu import gamemenu
    from misc.plstats import player_stats
    print("\nYou packed your gym shorts, protein shake and headed to your local gym.")
    print("\nYour current stats are: \n\n","Looks =",player_stats[0],"\n Jacked =",player_stats[1],"\n Attraction =",player_stats[2],"\n")
    excerciseTime = int(input("\nhow long do you wish to excercise for? Use seconds: "))
    if excerciseTime > 20:
        print("\nyou can not excercise for more than 20 seconds!")
        gymExcercise()
    else:
        player_stats[1] = player_stats[1] + excerciseTime
        for l in range(excerciseTime-1):
            print("💪")
            sleep(1)
        print()
        sleep(excerciseTime)
        print("\nyou got closer to being an absolute CHAD, good work chap. Your new stats are\n")
        print("\nYour current stats are: \n\n","Looks=",player_stats[0],"\n Jacked=",player_stats[1],"\n Attraction=",player_stats[2],"\n")
        gamemenu()
    
  

