expense={}
expenses=[]
def addExpense(expense):
  expenses.append(expense)
  return
  
def viewExpense():
  if not expenses:
    print("No expenses to show")
    return
  print("_____Your expenses_____")
  for expense in expenses:
    print("{:<10} -> {}".format(expense['Name'],expense['Amount']))
  return

def totalSpent():
  total=0
  for expense in expenses:
    total+=expense['Amount']
  print("The total amount spent: ",total)
  return

while True:
  print()
  print("______Expense Tracker Menu______")
  print("Enter 1 to add an expense")
  print("Enter 2 to view all expenses")
  print("Enter 3 to view total spent")
  print("Enter 4 to exit")
  print()
  
  num=int(input("Enter a num :"))
  if num==1:
      num2=int(input("Enter no. of expenses "))
      for i in range(num2):
        Name=input("Name of expense : ")
        amount=int(input("Enter amount spent : "))
        expense={'Name': Name,'Amount':amount}
        addExpense(expense)
  elif num==2:
      viewExpense()
  elif num==3:
      totalSpent()
  elif num==4:
      print("Exited")
      break
  else:
    print("Invalid. Please enter 1-4")






