#Rizzsim_0.0.2
#KrpanKodingKompany, All rights reserved 2022
from woman_intro import miaIntr, emmaIntr, lanaIntr, janeIntr
from stats import player_stats
from time import sleep
from random import choice
#hopefully this expands
#woman_list = ["Mia", "Emma", "Lana", "Jane", "Jenny", "Anna", "Mimi", "Lina", "Anya"]
woman_list = ["Mia"]
#test if woman picker works correctly
woman = (choice(woman_list))

def interactions():
    if (woman == "Mia"):
        if player_stats >= [20,25,2] : 
            print(miaIntr)
            sleep(10)
            accept_mia = input(f"do you wish to continue Mia's story? If so, type yes ")
            if (accept_mia == "yes" or "y"):
                print('you are walking down the hallway on your first day of college, when you look behind you and spot one of if not the most beautiful girl you have ever seen, walking behind you. You just can\'t take your eyes off of her and because you are walking with your head turned backwards, you bump into some poor guy who was just minding his buisness. Everything you are holding falls on the ground and you scramble to pick it all up. Suddenly a soft angelic voice asks you "hey, may I help you?" it\'s her! The beautifull tall motherly girl that caused you to drop all of your stuff. you become so flustered that you can\'t answer, watching as she picks your stuff up into a neat pile. "Here you go" she says with a smile on her stunning face. Before you have the chance to say anything she leaves just as the bell rings.')
            else: interactions()
        else: interactions() 
"""
    elif (woman == "Emma"):
        if (looks>34, jacked>25, attraction>3):
            print(emmaIntr)
        else: interactions()
    elif (woman == "Lana"):
        if (looks>30, jacked>25, attraction>3):
            print(lanaIntr)
        else: interactions()
    elif (woman == "Jane"):
        if (looks>25, jacked>20, attraction>2):
            print(janeIntr)
        else: interactions()
    elif (woman == "Jenny"):
        print("Jenny: true")
    elif (woman == "Anna"):
        print("Anna: true")
    #test intro. wont be used later on 
    elif (woman == "Mimi"):
        if (looks>10, jacked>10, attraction>1):
            print("i Really like you")
        else: interactions()
    elif (woman == "Lina"):
        print("Lina: true")
    elif (woman == "Anya"):
        print("Anya: true")
"""
interactions()





"""
Credits:
Maj - Lead programmer, spell checker
Gorazd - Lead Writer, code review, idea provider
"""