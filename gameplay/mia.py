from time import sleep
from misc.mainmenu import gamemenu
from stories import woman_intro as wi, MiaStories as ms

def levelneeded():
    global mialvl
    mialvl = [20,20,2]
    return(mialvl)

def miaintro():
    print(wi.miaIntr)
    sleep(10)
    miacontinue = input("Do you wanna continue Mia's story, if so type yes\n ")
    if miacontinue == "yes":
        sleep(5)
        miaFirstStory()

def miaStory2():
    miacontinue = input("Do you wanna continue Mia's story, if so type yes\n ")
    if miacontinue == "yes":
        sleep(2)
        miaSecondStory()
    
    else:
       gamemenu() 


def miaFirstStory():
    print(ms.MiaStory1)
    sleep(10)

def miaSecondStory():
    print(ms.MiaStory2)
    gamemenu()
    sleep(10)
