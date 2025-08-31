import random
print("____Number Guessing name____")

while True:
    won=0
    random_no = random.randint(1,50)
    for i in range(5,0,-1):
        print()
        print("{} chances are left".format(i))
        try:
           no = int(input("Guess the number from 1 to 50: "))
        except ValueError:
            print("Enter numberss daa :(")
            continue
        if no>random_no and i>1:
           print("Go a bit lower")
        elif no<random_no and i>1:
           print("Go a bit higher")
        elif no==random_no:
           print("Yayyy U Wonn!!")
           won=1
           break

    if won==0:
       print("The correct number was {}".format(random_no))
       print("Uh oh u lost. Better luck next time :)")
    print()
    try:
       once_more=int(input("1 to play again and 0 to quit: "))
    except ValueError:
        print("Enter numberss daa :(")
        continue
    if once_more==0:
        print("Hope u enjoyed. Byeee...")
        break
    
