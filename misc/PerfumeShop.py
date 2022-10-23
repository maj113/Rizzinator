#coment cuz python dev :sunglasses:
from time import sleep
from misc.PLStats import player_stats
maxusagevar = [1]
#this will count to 3 and then tell goingtoshop() to stop increasing the attraction stat
def maxusage():
    maxusagevar[0] = maxusagevar[0] + 1

def goingToShop():
    from misc.MainMenu import slow_print, gamemenu   
    if maxusagevar[0] <= 3:
        maxusage()
        slow_print("You go shopping for perfume") 
        perfumes = ["\nChallen", "Bugo Hoss", "Rakija", "Juzza"]
        print(*perfumes)
        perfume_picked = input("\nWhich one of these perfumes do you wish to purchase? ").lower().strip()
        #the way it prints out perfumes is confusing 
        if perfume_picked == "challen":
            sleep(1)
            player_stats[2] = player_stats[2] + 1 
            slow_print(f"\nYou did a little perfume testing, and decided to pick \"Challen\". Your attraction stat is now: {player_stats[2]}") 
            gamemenu()
        elif perfume_picked == "bugo hoss":
            sleep(1)
            player_stats[2] = player_stats[2] + 1
            slow_print(f"\nYou do a little perfume testing, and decided to pick \"Bugo Hoss\". Your attraction stat is now: {player_stats[2]}")
            gamemenu()
        elif perfume_picked == "rakija":
            sleep(1)
            player_stats[2] = player_stats[2] + 1
            slow_print(f"\nYou tried out the parfumes that were offered to you, and decided they smell girly. You went back home and rubbed some of grandpa's rakija on yourself. Your attraction stat is now: {player_stats[2]}")
            gamemenu()
        elif perfume_picked == "juzza":
            sleep(1)
            player_stats[2] = player_stats[2] + 1
            slow_print(f"\nYou took a look at the Juzza bottle and asked around if anyone knew what the hell Juzza is. Much to your dissapointment no one knew what it was and the cashier said it isn't even in their inventory. Nevertheless you now smell like raspberies and creampie. Your attraction stat is now: {player_stats[2]}")
            gamemenu()
        else:
            slow_print("\nYou ventured to the very back of the shop, picked out a nice bottle of perfume, walked up to the cashier, took out your lighter and in a matter of seconds created a makeshift flamethrower, with which you melted the poor cashiers face off in an instant. Try again")
            sleep(1)
            gamemenu()
    else:
        print("You applied so much perfume that everyone in your vicinity dropped like a fly. You were promptly escorted out of the shop.")
        gamemenu()
