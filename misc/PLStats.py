from random import randint

#dont call the function more than once as it will override the var 
def playername():
    global PlayerName
    player = input(str("what is your name? "))
    PlayerName = player
    if PlayerName == "god":
        player_stats[0] = player_stats[0] + 100
        player_stats[1] = player_stats[1] + 100
        player_stats[2] = player_stats[2] + 100
    
#this will randomize Player_stats so call it only once, then call the variable
def stats1():
    global player_stats
    player_stats = [randint(10,100), randint(10,100), randint(1,5)] #looks. jacked, attraction
    return(player_stats)
stats1()
