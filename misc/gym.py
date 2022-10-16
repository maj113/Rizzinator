#random comment cause this is what devs do... right?

import sys
from time import sleep
from random import randint


def gymExcercise():
    print("You packed your gym shorts, protein shake and headed to your local gym.")
    print("your current stats are")
    from misc.plstats import player_stats
    print(player_stats)
    excerciseTime = int(input("how long do you wish to excercise for? Use seconds: "))
    maxExcerciseTime = 20
    if excerciseTime > maxExcerciseTime:
        print("you can not excercise for more than 20 seconds!")
        gymExcercise()
    else:
        print(player_stats)
        player_stats[1] = player_stats[1] + excerciseTime
        sleep(excerciseTime)
        print(f"you got closer to being an absolute CHAD, good work chap. Your new stats are")
    print(player_stats)
    

