#Calculator using function

def add():
    a = int(input("Enter Number: "))
    b = int(input("Enter Number: "))
    addition = a + b
    print(addition)

def subtraction():
    a = int(input("Enter Number: "))
    b = int(input("Enter Number: "))
    subtraction = a - b
    print(subtraction)

def multiply():
    a = int(input("Enter Number: "))
    b = int(input("Enter Number: "))
    Multiply = a*b
    print(Multiply)

def divide():
    a = int(input("Enter Number: "))
    b = int(input("Enter Number: "))
    divide = a/b
    print(divide)

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter choice: "))
    
    a = int(input("Enter Number: "))
    b = int(input("Enter Number: "))

    if choice == 1:
       add()

    elif choice == 2:
        subtraction()

    elif choice == 3:
        multiply()

    elif choice == 4:
        divide()

    elif choice == 5:
        break

    else:
        print("Invalid choice")
