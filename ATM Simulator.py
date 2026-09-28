#=====ATM=====
#Check Balance
#Deposit
#Withdraw
#Exit
Balance = 10000000
print("Your balance is:",Balance)

while True: 
    print("\nChoose option")
    print("1.Check Balance")
    print("2.Withdrawn")
    print("3.Deposit")
    print("4.Exit")

    Choice = int(input("Enter choice Number: "))
    if(Choice==1):
       CurrentBalance = Balance
       print(CurrentBalance)

    elif Choice==2:
       Drawing = int(input("Enter Amount:"))
       if Drawing<= Balance:
          print("Withdrawal Successful")
          Balance = Balance-Drawing
          print("Remaining Balance:",Balance)
       else:
           print("Insufficient Balance")

    elif(Choice==3):
        Deposit =int(input("Enter the amount: "))
        Balance = Balance+Deposit
        print("Deposit Successful")
        print("New Balance:",Balance)

    elif(Choice==4):
        print("Thanks to use me")
        break

    else:
        print("Invalid choice")


    
    

 