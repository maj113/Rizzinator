from random import randint

#this will randomize Player_stats
def stats1():
    global player_stats
    player_stats = [randint(10,100), randint(10,100), randint(1,5)] #looks. jacked, attraction
    return(player_stats)
