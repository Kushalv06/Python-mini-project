import random 
Moves=['rock','paper','scissors']

while True:
    comp=random.choice(Moves)
    print()
    print("Make your choice")
    print()
    user=input("Rock Paper Scissors: ").lower()
    if user not in Moves:
        print("Enter a valid input.")
        continue

    if user==comp:
        print(f"Player : {user}")
        print(f"Computer : {comp}")
        print("Draw")
    elif user=="rock" and comp=="scissors":
        print(f"Player : {user}")
        print(f"Computer : {comp}")
        print("yayy U won!!")
    elif user=="paper" and comp=="rock":
        print(f"Player : {user}")
        print(f"Computer : {comp}")
        print("Yayy U won!!")
    elif user=="scissors" and comp=="paper":
        print(f"Player : {user}")
        print(f"Computer : {comp}")
        print("Yayy U won!!")
    else:
        print(f"Player : {user}")
        print(f"Computer : {comp}")
        print("Uh oh U lost :(")
    
    print()
    user=input("Do u wanna play again....1 to continue & 0 to quit: ")
    
    if user=='0':
        print("Hope u enjoyedd")
        break
    
        


