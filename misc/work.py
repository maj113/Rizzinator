from time import sleep

def GoToWork():
    from misc.MainMenu import gamemenu, slow_print
    from misc.PLStats import money
    slow_print("\nYou decide to finally show up for work, \"Look who finally came to work!\" Says your manager.")
    print(f"\nYou are broke asf and only have {money[0]} bucks")
    worktime = int(input("\nhow long is your shift? Use seconds: "))
    if worktime > 60:
        slow_print("\nyou can not work for more than 60 seconds!", speed=4)
        GoToWork()
    else:
        money[0] = money[0] + (worktime*3)
        for l in range(worktime):
            print("🤓 ", flush = True,end="")
            sleep(1)
        print()
        slow_print(f"\nYou FINALLY finish your shift and get {worktime*3} bucks, in total you now have {money[0]} \n")
        gamemenu()
    
  

