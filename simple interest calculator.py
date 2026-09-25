#Calculate simple interest and total amount.
Principal = int(input("Enter the Amount: "))
Rate = int(input("Rate of Interest: "))
time = int(input("Enter time: "))
print("Simple interest")
Calculate = (Principal*Rate/100*time)
print(Calculate)
TotalAmount = Principal + Calculate
print("Total Simple interest")
print(TotalAmount)
