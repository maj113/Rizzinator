from time import sleep
from tkinter import Misc


from stories import woman_intro as wi, MiaStories as ms
def levelneeded():
    global mialvl
    mialvl = [20,20,2]
    return(mialvl)

def miaintro():
    print(wi.miaIntr)
    sleep(10)
    miacontinue = input("Do you wanna continue Mia's story, if so type yes ")
    print(miacontinue)
    if miacontinue == "yes":
        sleep(5)
        miafirststory()
    else: 
        from misc.mainmenu import gamemenu
        gamemenu()  

def miafirststory():
    print(ms.MiaStory1)
    sleep(10)
