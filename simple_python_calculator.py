def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  if b != 0:
    return a/b
  else:
    return "denomenator cannot be 0"

while True:
    while True:
        first_num = input("Please enter your first number: ")
        if first_num.lower() == "exit":
            print("Thanks for playing!")
            exit()
        try:
            num1 = float(first_num)
            break
        except ValueError:
            print("Please enter a valid first number")

    while True:
        second_num = input("please enter your second number: ")
        if second_num.lower() == "exit":
            print("Thanks for playing!")
            exit()
        try:
            num2 = float(second_num)
            break
        except ValueError:
            print("Please enter a valid second number")

    choice = input("Please choose the operator '+','-','*','/'")
    if choice == '+':
        print(f'Result is {add(num1,num2)}')
    elif choice == '-':
        print(f'Result is {sub(num1,num2)}')
    elif choice == '*':
        print(f'Result is {mul(num1,num2)}')
    elif choice == '/':
        print(f'Result is {div(num1,num2)}')            
    elif choice.lower() == "exit":
        print("Thanks for Playing!")
        exit()
    else:
        print("Please enter valid operator")

        
