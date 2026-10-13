#Mini toolkit
while True:
    print("1.Calculator")
    print("2.Temperature convertor")
    print("3.Age Guessing Trick")
    print("4.Word Counter")
    print("5.Exit")

    Choice = int(input("Enter your choice: "))

    if(Choice==1):
        print("----Calculator----")
        def add():
            a = int(input("Enter Number: "))
            b = int(input("Enter another Number:  "))
            Sum = a + b
            print(Sum)
        def sub():
            a = int(input("Enter number: "))
            b = int(input("Enter another Number: "))
            subtraction = a - b
            print(subtraction)
        def divide():
            a = int(input("Enter number: "))
            b = int(input("Enter number: "))
            division = a/b
            print(division)
        def multiply():
            a = int(input("Enter number: "))
            b = int(input("Enter number: "))
            multiplication = a*b
            print(multiplication)

        
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Enter choice: "))
    
          

        if choice == 1:
             add()

        elif choice == 2:
             sub()

        elif choice == 3:
             multiply()

        elif choice == 4:
             divide()

        elif choice == 5:
              break

        else:
           print("Invalid choice")

    if(Choice==2):
         print("----Temerature Convertor----")
         print("=== Temperature Converter ===")
         print("1. Celsius to Fahrenheit")
         print("2. Fahrenheit to Celsius")

         choice = input("Choose an option: ")

         if choice == "1":
           celsius = float(input("Enter temperature in Celsius: "))
           fahrenheit = (celsius * 9 / 5) + 32
           print("Temperature in Fahrenheit:", fahrenheit)

         elif choice == "2":
           fahrenheit = float(input("Enter temperature in Fahrenheit: "))
           celsius = (fahrenheit - 32) * 5 / 9
           print("Temperature in Celsius:", celsius)

         else:
           print("Invalid choice!")

    if(Choice==3):
          
         print("=== Age Guessing ===")

         birth_year = int(input("Enter your birth year: "))

         age = 2026 - birth_year

         print("Your age is:", age)

    if(Choice==4):
        
        print("=== Word Counter ===")

        text = input("Enter your text: ")

        words = text.split()

        word_count = len(words)

        print("Total words:", word_count)

    if(Choice==5):
        print("5.EXIT")
        print("Thanks for using me")
        break