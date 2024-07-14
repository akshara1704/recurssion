import random
stone=1
paper=2
scissor=3
pc= random.randrange(1,4)
num=int(input("enter 1 for stone,2 for paper and 3 for scissor= "))
if num<=3 and num>=1:
    if num==pc:
        print("DRAW")
    elif pc==1:
        if num==2:
            print("YOU WIN")
        if num==3:
            print("YOU LOST")
    elif pc==2:
        if num==1:
            print("YOU LOST")
        if num==3:
            print("YOU WIN")
    elif pc==3:
        if num==1:
            print("YOU WIN")
        if num==2:
            print("YOU LOST")
    print("pc selected this number=",pc)
else:
    print("select between 1 to 3")