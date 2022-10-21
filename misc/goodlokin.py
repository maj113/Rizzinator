#coment cuz python dev :sunglasses:

from time import sleep
import mainmenu as mm
import plstats as ps

def goingToShop():
    print("You go shoping for perfum") #temporary text cuz lazy
    perfumes = ["Challen", "Bugo Hoss", "Rakija", "Juzza"]
    perfume_picked = input("Which one of these perfumes do you wish to purchase? ")

    if perfume_picked == "Challen":
        sleep(1)
        ps.player_stats[2] +1 #to zih ne dela 
        print("You did a little perfume testing, and decided to pick \"Challen\".", ps.player_stats[2]) #only god knows if this works :skull:
    elif perfume_picked == "Bugo Hoss":
        sleep(1)
        ps.player_stats[2] +1
        print("You do a little perfume testing, and decided to pick \"Bugo Hoss\".", ps.player_stats[2])
    elif perfume_picked == "Rakija":
        sleep(1)
        ps.player_stats[2] +1
        print("You tried out the parfumes that were offered to you, and decided they smell girly. You went back home and rubbed some of grandpa's rakija on yourself.", ps.player_stats[2])
    elif perfume_picked == "Juzza":
        sleep(1)
        ps.player_stats[2] +1
        print("You took a look at the Juzza bottle and asked arround if anyone knew what the hell Juzza is. Much to your dissapointment no one knew what it was and the cashier said it isn't even in their inventory. Nevertheless you now smell like raspberies and creampie.", ps.player_stats[2])
    else:
        print("You ventured to the very back of the shop, picked out a nice bottle of perfume, walked up to the cashier, took out your lighter and in a matter of seconds created a makeshift flamethrower, with which you melted the poor cashiers face off in an instant. Try again")
        sleep(1)
        mm.gamemenu()
