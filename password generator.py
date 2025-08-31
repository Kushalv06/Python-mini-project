import random

alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
special="!@#$&*"
while True:
    print()
    print("-------Password generator-------")
    choice=""
    password=[]
    length=(input("Enter number of characters: "))
    print()
    if length.isdigit():
        length=int(length)
    else:
        print("Enter a valid input")
        continue

    print("1.Only Numbers")
    print("2.Only alphabets")
    print("3.Alphabets + Numbers")
    print("4.Alphabets + Special Characters")
    print("5.Alphabets + Special Characters + Numbers")
    num=input("What combination do u need? Enter number: ")
    print()

    if num=='1':
        choice=numbers
        for i in range(length):
            password.append(random.choice(choice))
    elif num=='2':
        choice=alphabets
        for i in range(length):
            password.append(random.choice(choice))
    elif num=='3':
        choice=alphabets+numbers
        for i in range(length):
            password.append(random.choice(choice))
    elif num=='4':
        choice=alphabets+special
        for i in range(length):
            password.append(random.choice(choice))
    elif num=='5':
        choice=alphabets+special+numbers
        for i in range(length):
            password.append(random.choice(choice))
    else:
        print("Enter a valid option")
        continue

    password=''.join(password)
    print("The generated password is: {}".format(password))

    change=input("Do u wanna change it?(nahh/1): ")
    if change!='1':
        print("Thank Youu!!")
        break
        print()

            
                


        

        

