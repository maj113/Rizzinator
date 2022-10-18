from time import sleep
from stories import woman_intro as wi, MiaStories as ms
from misc.mainmenu import gamemenu

def levelneeded():
    global mialvl
    mialvl = [20,25,2]
    return(mialvl)

def miaintro():
    print(wi.miaIntr)
    sleep(5)
    miacontinue = input("Do you wanna continue Mia's story, if so type yes\n ")
    if miacontinue == "yes":
        sleep(5)
        print(ms.MiaStory1)
        sleep(5)
        miacontinue = input("Do you wanna continue Mia's story, if so type yes\n ")
        if miacontinue == "yes":
            sleep(2)
            miaSecondStory()
        else:
                gamemenu()
    else:
        gamemenu()

def miaSecondStory():
    print(ms.MiaStory2)
    sleep(2)
    print(ms.miaAskOut1,"\n", ms.miaAskOut2,"\n", ms.miaAskOut3)
    selectedInteraction = int(input("\nWhich of these three pick up lines do you wish to use on Mia? input numbers 1, 2 or 3 \n"))
    sleep(2)
    if selectedInteraction == 1:
            print(ms.miaReaction1)
        
    elif selectedInteraction == 2:
            print(ms.miaReaction2)
        
    elif selectedInteraction == 3:
            print(ms.miaReaction3)
        
    elif selectedInteraction >= 4:
            print("BRO 4 AND ABOVE WASN'T AN OPTION!!!")
            gamemenu()

    


