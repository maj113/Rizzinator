from time import sleep
from stories import MiaStories as ms
from misc.mainmenu import gamemenu, slow_print

def levelneeded():
    global mialvl
    mialvl = [20,25,2]
    return(mialvl)

def miaintro():
    slow_print(ms.miaIntr)
    sleep(2)
    miacontinue = input("Do you wanna continue Mia's story, if so type yes\n ")
    if miacontinue == "yes":
        sleep(2)
        slow_print(ms.MiaStory1)
        sleep(2)
        miacontinue = input("Do you wanna continue Mia's story, if so type yes\n ")
        if miacontinue == "yes":
            sleep(2)
            miaSecondStory()
            sleep(2)
            miacontinue = input("Do you wanna continue Mia's story, if so type yes\n ")
        if miacontinue == "yes":
            sleep(2)
            miaThirdStory()
        else:
                gamemenu()
    else:
        gamemenu()

def miaSecondStory():
    slow_print(ms.MiaStory2)
    sleep(2)
    print(ms.miaAskOut1,"\n", ms.miaAskOut2,"\n", ms.miaAskOut3)
    selectedInteraction = int(input("\nWhich of these three pick up lines do you wish to use on Mia? input numbers 1, 2 or 3 \n"))
    sleep(2)
    if selectedInteraction == 1:
            slow_print(ms.miaAskOut1)
            sleep(1)
            slow_print(ms.miaReaction1)
        
    elif selectedInteraction == 2:
            slow_print(ms.miaAskOut2)
            sleep(1)
            slow_print(ms.miaReaction2)
        
    elif selectedInteraction == 3:
            slow_print(ms.miaAskOut3)
            sleep(1)
            slow_print(ms.miaReaction3)
        
    elif selectedInteraction >= 4:
            slow_print("BRO 4 AND ABOVE WASN'T AN OPTION!!!", speed=5)
            gamemenu()

    
def miaThirdStory():
    slow_print(ms.MiaStory3)
    sleep(2)
    print(ms.miaAns1,"\n", ms.miaAns2,"\n", ms.miaAns3)
    selectedInteraction = int(input("\nWhich of these three interactions do you wish to use? input numbers 1, 2 or 3 \n"))
    sleep(2)
    if selectedInteraction == 1:
            slow_print(ms.miaAns1)
            sleep(1)
            slow_print(ms.miaReact1)
        
    elif selectedInteraction == 2:
            slow_print(ms.miaAns2)
            sleep(1)
            slow_print(ms.miaReact2)
        
    elif selectedInteraction == 3:
            slow_print(ms.miaAns3)
            sleep(1)
            slow_print(ms.miaReact3)
        
    elif selectedInteraction >= 4:
            slow_print("BRO 4 AND ABOVE WASN'T AN OPTION!!!", speed=5)
            gamemenu()

