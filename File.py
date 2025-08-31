#Merge conflict
#Lets see what happens
def add_note():
    file=open("Notes.txt",'a')
    print()
    note=input("Enter the notes")
    file.write(note + "\n")
    file.close()
    
def view_notes():
    file=open("Notes.txt",'r')
    for i,note in enumerate(file,start=1):
        print(f"{i}.{note}",end='')
    print()
    file.close()

def delete_notes():
    file=open("Notes.txt",'w')
    file.close()
    print("Deleted")

def main():
    print("---------Notes App---------")
    print()
    while True:
        print("1.Add a note")
        print("2.View all notes")
        print("3.Delete all notes")
        print("4.Exit")
        print()
        num=input("Enter your choice number: ")

        if num=='1':
            add_note()
        elif num=='2':
            view_notes()
        elif num=='3':
            delete_notes()
        elif num=='4':
            break
        else:
            print("Enter a valid input :(")
            continue
    
if __name__ == "__main__":
    main()