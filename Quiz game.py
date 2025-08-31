questions=[{'question':'2 + 2 =','options':'A.5, B.6, C.4, D.2','answer':'C'},
           {'question':'4 + 5 =','options':'A.9, B.1, C.7, D.3','answer':'A'},
           {'question':'9 + 1 =','options':'A.1, B.0, C.10, D.8','answer':'C'},
           {'question':'3 + 4 =','options':'A.6, B.7, C.8, D.9','answer':'B'},
           {'question':'1 + 1 =','options':'A.1, B.3, C.4, D.2','answer':'D'}]

import random
while True:
    random.shuffle(questions)
    
    print("CHOOSE THE CORRECT ANSWERS")
    score=0
    guesses=[]
    for i,question in enumerate(questions,start=1):
        print("----------------------------")
        print()
        print(f"{i}. {question['question']}")
        print(question['options'])
        answer=input().upper()
        if answer != "A" or "B" or "C" or "D":
            print("Enter a valid option")
            print("You lost one point :(")
        guesses.append(answer)
        if answer==question['answer']:
            score+=1
            print("CORRECT")
        else:
            print("WRONG")

    print()
    print(f"Answers : ",end="")
    for question in questions:
        print(question['answer'],end=" ")
    print()
    print("Guesses : ",end="")
    for guess in guesses:
        print(guess,end=" ")
    print()
    print(f"Your total score is {score}/5")
    percent=score/5 * 100
    print("Percentage : {}%".format(percent))
    if(score==5):
        print("Congrats you got all correct")
    print()
    play=input("Wanna play again?(y/n): ").lower()
    if play != "y":
        print("Have a good dayy....Byeee")
        break
