#Rizzsim_0.0.2
#KrpanKodingKompany, All rights reserved 2022
from random import choice, randint
from time import sleep
#hopefully this expands
#woman_list = ["Mia", "Emma", "Lana", "Jane", "Jenny", "Anna", "Mimi", "Lina", "Anya"]
woman_list = ["Mia"]
#test if woman picker works correctly 
player = input(str("what is your name little boy? "))
def interactions():
    woman = (choice(woman_list))
    looks = randint(10,100)
    attraction = randint(1,5)
    jacked = randint(10,100)
    if (woman == "Mia"):
        if (looks>15, jacked>20, attraction>3):
            print("Hi I'm Mia and I'm 18 and a half. I've always been the tall girl and I was sometimes even bullied for it. I kind of get it I mean I'm 6ft4\" (195cm). I have gray eyes, brown long hair, and I like to wear dark clothes. I'm usually really calm and everyone says my voice is really calming. But anyway, I like to paint, draw and play guitar. I listen to classical music while I paint because it helps me focus and gives me inspiration. I'm a pretty reserved person though.")
            sleep(10)
            accept_mia = input(f"do you wish to continue Mia's story? If so, type yes ")
            if (accept_mia == "yes" or "y"):
                print('you are walking down the hallway on your first day of college, when you look behind you and spot one of if not the most beautiful girl you have ever seen, walking behind you. You just can\'t take your eyes off of her and because you are walking with your head turned backwards, you bump into some poor guy who was just minding his buisness. Everything you are holding falls on the ground andyou scramble to pick it all up. Suddenly a soft angelic voice asks you "hey, may I help you?" it\'s her! The beautifull tall motherly girl that caused you to drop all of your stuff. you become so flustered that you can\'t answer, watching as she picks your stuff up into a neat pile. "Here you go" she says with a smile on her stunning face. Before you have the chance to say anything she leaves just as the bell rings.')
            else: interactions()
        else: interactions() 
    elif (woman == "Emma"):
        if (looks>34, jacked>25, attraction>3):
            print(" I'm Emma and I'm 20 years old. I have black hair but Half of it is painted dark red lol. I dress goth, that means I have a nose piercing I wear black makeup and wear eyeliner. I also like to wear fishnets and a black skirt which I ussualy pair with a black croptop. I have hazel eyes and a lot of freckles all over my face. I'm really tall. About 185cm. I love playing videogames and I like listening to Radiohead and Nirvana.")
        else: interactions()
    elif (woman == "Lana"):
        if (looks>30, jacked>25, attraction>3):
            print("Sup I'm lana. I'm 19. I have dark blonde hair which reaches to my shoulders. My eyes are blue and I have freckles. I'm about 165cm tall and I like to wear vibrant clothes. I'm always optimistic and I'm rarely anxious or sad. I like to go to parties and other social events.")
        else: interactions()
    elif (woman == "Jane"):
        if (looks>25, jacked>20, attraction>2):
            print("Hello I'm Jenny and I'm 18. I have Green eyes and green hair, and I'm really tall, about 190cm. I curl my hair up like Tatsumaki from One Punch Man, tho my figure is more like Fubuki's 😉 I like to read manga ans watch anime whenever I'm not studying.")
        else: interactions()
    elif (woman == "Jenny"):
        print("Jenny: true")
    elif (woman == "Anna"):
        print("Anna: true")
    elif (woman == "Mimi"):
        if (looks>10, jacked>10, attraction>1):
            print("i Really like you")
        else: interactions()
    elif (woman == "Lina"):
        print("Lina: true")
    elif (woman == "Anya"):
        print("Anya: true")
interactions()




"""
credits:
Maj - Lead programmer, spell checker
Gorazd - Lead Writer, code review, idea provider
"""