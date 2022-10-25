#random comment cause this is what devs do... right?
from time import sleep
from misc.PLStats import player_stats, money

def gymExcercise():
    from misc.MainMenu import gamemenu, slow_print
    from misc.PLStats import player_stats, money
    slow_print("\nYou packed your gym shorts, protein shake and headed to your local gym.")
    print(f"Your current jacked stat is {player_stats[1]}, and {money}$")
    excerciseTime = int(input("\n You have how long do you wish to excercise for? Use seconds! (1 second is 2$) "))
    if excerciseTime > 20:
        slow_print("\nyou can not excercise for more than 20 seconds!", speed=4)
        gymExcercise()
    else:
        #this needs to be improved, @Gorchii please improve 
        player_stats[1] = player_stats[1] + excerciseTime
        money = money - (excerciseTime*2)
        for l in range(excerciseTime):
            print("💪 ", flush = True,end="")
            sleep(1)
        print()
        slow_print(f"\nyou got closer to being an absolute CHAD, good work chap. You now have {money}$. But it was worth it, and your new stats are\n")
        print("Looks=",player_stats[0],"\n Jacked=",player_stats[1],"\n Attraction=",player_stats[2],"\n")
        gamemenu()
    
  

