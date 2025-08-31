
contacts=[]
contact={}

def add_contact():
    no=int(input('Enter number of contacts: '))
    for i in range(no):
        name=input("Enter name: ").lower()
        num=int(input("Enter number: "))
        contact={'Name':name,'Number':num}
        contacts.append(contact)
        print("Done")
        print()

def view_contact():
    length=len(contacts)
    if not contacts:
        print()
        print("---Nothing to show here---")
        return
    print(f"Total number of contacts: {length}")
    for i,contact in enumerate(contacts,start=1):
        print(f"{i}.Name   : {contact['Name']}")
        print(f"  Number : {contact['Number']}")
        print()
    print("________End________")

def search_contact():
    num=0
    search=input("Enter name to search: ").lower()
    for contact in contacts:
        if contact['Name']==search:
            num=1
            print(f"Name   : {contact['Name']}")
            print(f"Number : {contact['Number']}")
            print()
            break
    if num==0:
        print("Not found")
    
def delete_contact():
    num=0
    delete=input("Enter name to delete: ").lower()
    for contact in contacts:
        if contact['Name']==delete:
            contacts.remove(contact)
            num=1
            print("Done")
            print()
            break
    if num==0:
        print("Not found")
        print()

while True:
    print()
    print("______Contact List______")
    print()
    print("1.Add contact")
    print("2.View all contacts")
    print("3.Search a contact")
    print("4.Delete a contact")
    print("5.exit")
    print()
    choice=(input("Enter a choice: "))
    if choice.isdigit():
        choice=int(choice)
        if choice==1:
            add_contact();
        if choice==2:
            view_contact();
        if choice==3:
            search_contact();
        if choice==4:
            delete_contact();
        if choice==5:
            print("Thank you!!")
            break
    else:
        print("Enter a valid input")




        
    
    
