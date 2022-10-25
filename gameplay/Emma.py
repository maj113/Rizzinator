from time import sleep
from stories import EmmaStories as ms

emmalvl = [25,30,3]
#emmaintro() needs to be refined, as-is saving in impossible.
emmasaves = []
def emmaintro():
    from misc.MainMenu import gamemenu, slow_print
    slow_print(ms.emmaIntr,speed=8)
    sleep(1)
    emmasaves.append("intro")
    emmacontinue = input("Do you wanna continue emma's story, if so type yes\n ")
    if emmacontinue == "yes":
        emmaFirstStory()
    else: gamemenu()


def emmaFirstStory():
    from misc.MainMenu import gamemenu, slow_print
    sleep(1)
    slow_print(ms.emmaStory1,speed=8)
    emmasaves.append("1st story")
    sleep(1)            
    emmacontinue = input("Do you wanna continue emma's story, if so type yes\n ")
    if emmacontinue == "yes":
        emmaSecondStory()     
    else: gamemenu()
        
          
def emmaSecondStory():
    from misc.MainMenu import gamemenu, slow_print
    slow_print(ms.emmaStory2,speed=8)
    sleep(1)
    print(ms.emmaAskOut1,"\n", ms.emmaAskOut2,"\n", ms.emmaAskOut3)
    selectedInteraction = int(input("\nWhich of these three pick up lines do you wish to use on emma? input numbers 1, 2 or 3 \n"))
    emmasaves.append("2nd story")
    sleep(1)
    if selectedInteraction == 1:
            slow_print(ms.emmaAskOut1, speed=8)
            sleep(1)
            slow_print(ms.emmaReaction1)
        
    elif selectedInteraction == 2:
            slow_print(ms.emmaAskOut2)
            sleep(1)
            slow_print(ms.emmaReaction2)
        
    elif selectedInteraction == 3:
            slow_print(ms.emmaAskOut3)
            sleep(1)
            slow_print(ms.emmaReaction3)
        
    elif selectedInteraction >= 4:
            slow_print("BRO 4 AND ABOVE WASN'T AN OPTION!!!", speed=5)
            gamemenu()

    
def emmaThirdStory():
    from misc.MainMenu import gamemenu, slow_print    
    slow_print(ms.emmaStory3)
    sleep(1)
    print(ms.emmaAns1,"\n", ms.emmaAns2,"\n", ms.emmaAns3)
    selectedInteraction = int(input("\nWhich of these three interactions do you wish to use? input numbers 1, 2 or 3 \n"))
    sleep(1)
    if selectedInteraction == 1:
            slow_print(ms.emmaAns1)
            sleep(1)
            slow_print(ms.emmaReact1)
        
    elif selectedInteraction == 2:
            slow_print(ms.emmaAns2)
            sleep(1)
            slow_print(ms.emmaReact2)
        
    elif selectedInteraction == 3:
            slow_print(ms.emmaAns3)
            sleep(1)
            slow_print(ms.emmaReact3)
        
    elif selectedInteraction >= 4:
            slow_print("BRO 4 AND ABOVE WASN'T AN OPTION!!!", speed=5)
            gamemenu()

