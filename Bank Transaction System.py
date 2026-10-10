Account ={}
Transactions=[]

def create_account():
    import random

    account_number = random.randint(1000, 9999)
    Account_holder_name = str(input("Enter your name: "))
    Initial_Deposit = int(input("Enter amount: "))

    Account[account_number] = {
        "Account_holder_name": Account_holder_name,
        "Initial_deposit": Initial_Deposit
    }

    print("\nAccount created successfully!")
    print("Account Number:", account_number)
    print("Account Holder:", Account_holder_name)
    print("Initial Deposit:", Initial_Deposit)

def view_account():
    print("1. View All Accounts")
    print("2. View Specific Account")

    view_choice = int(input("Enter view choice: "))

    if view_choice == 1:
        print("\n---- All Accounts ----")

        for account_number, details in Account.items():
            print("Account Number:", account_number)
            print("Account Holder:", details["Account_holder_name"])
            print("Balance:", details["Initial_deposit"])
            print("----------------------")

    elif view_choice == 2:
        enter_name = input("Enter Account Holder Name: ")
        found = False

        for account_number, details in Account.items():
            if details["Account_holder_name"].lower() == enter_name.lower():
                print("Account Number:", account_number)
                print("Account Holder:", details["Account_holder_name"])
                print("Balance:", details["Initial_deposit"])
                found = True
                break

        if found == False:
            print("Account not found!")

    else:
        print("Invalid choice!")
def deposit_money():
    print("---- Deposit Money ----")

    account_holder_name = str(input("Enter Account Holder Name: "))
    found = False

    for account_number, details in Account.items():
        if details["Account_holder_name"].lower() == account_holder_name.lower():
            amount = int(input("Enter Deposit Amount: "))

            details["Initial_deposit"] += amount
            Transactions.append(f"Withdrawal: Account {account_number}, Amount: {amount}")
            print("Deposit Successful!")
            print("Account Holder:", details["Account_holder_name"])
            print("New Balance:", details["Initial_deposit"])

            found = True
            break

    if found == False:
        print("Account not found!")
def withdraw_money():
    
    print("---- Withdraw Money ----")

    account_number = int(input("Enter Account Number: "))

    if account_number in Account:
        amount = int(input("Enter Withdrawal Amount: "))
        balance = Account[account_number]["Initial_deposit"]

        if amount <= balance:
            Account[account_number]["Initial_deposit"] -= amount
            Transactions.append(f"Withdrawal: Account {account_number}, Amount: {amount}")
            print("Withdrawal Successful!")
            print("Remaining Balance:", Account[account_number]["Initial_deposit"])

        else:
            print("Insufficient Balance!")

    else:
        print("Account not found!")

def transfer_money():
    print("----Transfer Money----")

    sender_name = str(input("enter sender account name: "))
    sender_found = False
    for sender_number , sender_details in Account.items():
         if sender_details["Account_holder_name"].lower() == sender_name.lower():
             sender_found = True
             break
    if sender_found== False:
        print("Your account not found")
        return
    receiver_name = input("Enter reciver account holder name: ")
    reciver_found =False

    for receiver_number, receiver_details in Account.items():
        if receiver_details["Account_holder_name"].lower() == receiver_name.lower():
            receiver_found = True
            break
    if receiver_found == False:
        print("Receiver Account Not Found!")
        return

    if sender_number == receiver_number:
        print("You cannot transfer money to yourself!")
        return

    amount = int(input("Enter Transfer Amount: "))

    sender_balance = sender_details["Initial_deposit"]

    if amount > 0 and amount <= sender_balance:
        sender_details["Initial_deposit"] -= amount
        receiver_details["Initial_deposit"] += amount

        Transactions.append({
           "account_number": sender_number,
           "type": "Transfer Sent",
           "amount": amount,
           "to": receiver_details["Account_holder_name"]
})

        Transactions.append({
           "account_number": receiver_number,
           "type": "Transfer Received",
           "amount": amount,
           "from": sender_details["Account_holder_name"]
})
        print("Transfer Successful!")
        print("Your Remaining Balance:", sender_details["Initial_deposit"])
        print("Receiver New Balance:", receiver_details["Initial_deposit"])

    else:
        print("Invalid Amount or Insufficient Balance!")


def transaction_history():
    
    print("---- Transaction History ----")
    account_holder_name = str(input("Enter account holder name: "))
    account_found = False
    for account_number ,details in Account.items():
        if details["Account_holder_name"].lower()== account_holder_name.lower():
            account_found = True
            break
        if account_found == False:
            print("Account not found")
            return
        transaction_found = False
        for transaction in Transactions:
            if transaction["account_number"] == account_number:
                print(transaction)
                transaction_found = True

            if transaction_found == False:
                print("No transaction")

    

        else:
           for transaction in Transactions:
            print(transaction)

while True:
    print("====BANK TRANSACTION SYSTEM====")
    print("1.Create Account")
    print("2.View Account")
    print("3.Deposit Money")
    print("4.Withdraw Money")
    print("5.Transfer_Money")
    print("6.Transaction History")
    print("7.Exit")

    Choice = int(input("ENTER CHOICE: "))
    if(Choice==1):
        create_account()
        
    elif Choice == 2:
        view_account()

    if(Choice==3):
        deposit_money()
    elif Choice==4:
        withdraw_money()

    elif Choice == 5:
        transfer_money()
    elif Choice == 6:
        transaction_history()
    elif Choice == 7:
        print("Thank for using me")
        break

           
                



