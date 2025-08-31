todolist=[]
tasks={}
def add_tasks():
    no=int(input("Enter no. of tasks"))
    for i in range(no):
        work=input("Enter the task to do: ")
        tasks={'Task':work,'Done':False}
        todolist.append(tasks)
    return

def view_tasks():
    if not todolist:
        print("Nothing to show")
        return
    for i,tasks in enumerate(todolist,start=1):
        if tasks['Done']:
            status="Done "
        else:
            status="Not yet done "
        print("{}. {} --> {}".format(i,tasks['Task'],status))
    return

def mark_task(numbers):
    for i in numbers:
        todolist[i-1]['Done']=True
        print("{} --> Marked as Done".format(todolist[i-1]['Task']))
    
    
def delete_task(user_input):
        print("{} --> Removed".format(todolist[i-1]['Task']))
        todolist.pop(i-1)
        
while True:
    print()
    print("Choose an option")
    print("1. Add tasks")
    print("2. View all tasks")
    print("3. Mark tasks as done")
    print("4. Delete tasks")
    print("5. Exit the program\n")

    choice=int(input("Enter your choice: "))
    if choice==1:
        add_tasks()
    elif choice==2:
        view_tasks()
    elif choice==3:
        if not todolist:
            print("Nothing to mark")
            continue
        user_input=input("Enter nums separeted by spaces")
        numbers=[int(num) for num in user_input.split()]
        mark_task(numbers)
    elif choice==4:
        if not todolist:
            print("Nothing to delete")
            continue
        user_input=input("Enter num to delete")
        delete_task(user_input)
    elif choice==5:
        print("Byee")
        break
    

        
        
    
