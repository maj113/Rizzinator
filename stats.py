from random import randint
player = input(str("what is your name? "))
#this will randomize Player_stats
def stats():
    global player_stats
    player_stats = [randint(10,100), randint(10,100), randint(1,5)]
    return(player_stats)

