from time import sleep


def loadsave():
    from misc.MainMenu import story_list, slow_print, gamemenu
    from gameplay.Mia import miasaves, miaintro, miaFirstStory, miaSecondStory
    slow_print(f"you can continue {story_list}'s story\n")
    savechoice1 = input("Which character's story do you want to continue? ").lower().strip()
    if savechoice1 not in story_list:
        menuchoice = input("\nYou cannot continue this story, do you want to go back to the main menu? ").strip().lower()
        if menuchoice == "yes":
            gamemenu()
        else: loadsave()
    elif savechoice1 == "mia":
        slow_print("Where do you want to continue? ")
        print(*miasaves,"\n")
        selsave = input().strip()
        print("\033[A                             \033[A") 
        if selsave in miasaves and "intro":
            miaintro()
        elif selsave in miasaves and "1st story":
            miaFirstStory()
        elif selsave in miasaves and "2nd story":
            miaSecondStory()
        else: 
            slow_print(f"You can't continue from {selsave}\n")
            sleep(1)
            gamemenu()