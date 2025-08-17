import random
L=["rock","paper","scissor"]
you_win=0
computer_win=0

while True:
    
    print("you win",you_win)
    print("computer win",computer_win)
    
    Ch=int(input('''
    1 YES
    2 NO OR EXIT
      '''))
    if Ch==1:
        print("You entered the game")
        for A in range(1,6):
            userinput=int(input('''
1 rock
2 paper
3 scissor
            '''))
            if userinput==1:
                print("you chose rock")
            elif userinput==2:
                print("you chose paper")
            elif userinput==3:
                print("you chose scissor")
            Cchoice=random.choice(L)
            print("Computer chose",Cchoice)
            if userinput==Cchoice:
                you_win += 1
                computer_win=computer_win+1
                print("Game Draw")
            elif (userinput=="rock" and Cchoice=="scissor") or (userinput=="paper" and Cchoice=="rock") or (userinput=="scissor" and Cchoice=="paper"):
                print("You Won")
                you_win=you_win+1
            else :
                print("Computer won")
                computer_win=computer_win+1
        print("your final score",you_win)
        print("Computer final score",computer_win)
    elif Ch==2:
        print("Thanks")
        break
    