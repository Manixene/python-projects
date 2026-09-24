# bill calculator.
print("Write the item")
purchases = str(input("item 1:"))
purchases = str(input("item 2:"))
purchases = str(input("item 3:"))
print("Tell the price")
price1 = float(input("item 1:"))
price2 = float(input("item 2:"))
price3 = float(input("item 3:"))
taxrate = int(input("tell the tax "))
subtotal = price1 + price2 + price3
print(subtotal)
Tax = subtotal * taxrate /100
final_total =  subtotal + Tax
print(final_total)

