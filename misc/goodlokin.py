#coment cuz python dev :sunglasses:
from time import sleep
from misc.plstats import player_stats

def goingToShop():
    from misc.mainmenu import slow_print, gamemenu 
    slow_print("\nYou go shoping for perfume") 
    perfumes = ["\nChallen", "Bugo Hoss", "Rakija", "Juzza"]
    slow_print(*perfumes, speed=5)
    perfume_picked = input("\nWhich one of these perfumes do you wish to purchase? ").lower()

    if perfume_picked == "challen":
        sleep(1)
        player_stats[2] = player_stats[2] + 1 #to zih ne dela 
        slow_print("\nYou did a little perfume testing, and decided to pick \"Challen\".", player_stats[2]) #only god knows if this works :skull:
    
    elif perfume_picked == "bugo hoss":
        sleep(1)
        player_stats[2] = player_stats[2] + 1
        slow_print("\nYou do a little perfume testing, and decided to pick \"Bugo Hoss\".", player_stats[2])
    
    elif perfume_picked == "rakija":
        sleep(1)
        player_stats[2] = player_stats[2] + 1
        slow_print("\nYou tried out the parfumes that were offered to you, and decided they smell girly. You went back home and rubbed some of grandpa's rakija on yourself.", player_stats[2])
    
    elif perfume_picked == "juzza":
        sleep(1)
        player_stats[2] = player_stats[2] + 1
        slow_print("\nYou took a look at the Juzza bottle and asked around if anyone knew what the hell Juzza is. Much to your dissapointment no one knew what it was and the cashier said it isn't even in their inventory. Nevertheless you now smell like raspberies and creampie.", player_stats[2])
    
    else:
        slow_print("\nYou ventured to the very back of the shop, picked out a nice bottle of perfume, walked up to the cashier, took out your lighter and in a matter of seconds created a makeshift flamethrower, with which you melted the poor cashiers face off in an instant. Try again")
        sleep(1)
        gamemenu()
