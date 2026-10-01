#Shopping Cart
list={
    "Clothes": ["Shirt", "Pants", "Jacket","Baggy Jeans","Cargo","T-shirts","Formal Pants"],
    "Electronics": ["Laptop", "smartphone", "Tablet", "Headphones", "Smartwatch", "camera", ],
    "Books": ["Fiction", "Non-Fiction", "Textbooks","self improvement","Business", "Magazines"],
    "Home & Kitchen": ["Blender", "Microwave", "Coffee Maker", "Toaster", "Kettle"]
}
Price = {
    "Clothes": [2000,2500,3000,1500,1800,1200,2200],
    "Electronics": [500000, 300000, 200000, 150000, 250000, 400000],
    "Books": [500, 700, 1000,800,600,400],
    "Home & Kitchen": [10000, 15000,8000,5000,6000]
}

cart = []
# Categories show
while True:
    print("==========SHOPPING CART==========")
    print("Available Categories:")

    for category in list:
        print(category)

 #category choose
    Category = input("\nChoose Category: ").strip().title()
    if Category not in list:
        print("Invalid category")
        continue
  
# Selected category ke items show
    print(f"\n{Category} Items:")
        
    for i, item in enumerate(list[Category]):
        print(f"{i+1}. {item} - ₹{Price[Category][i]}")

# User item choose kare
    choice = input("\nChoose item number(s) separeted by space: ")
    choice = choice.split()
    for choice in choice:
            item_choice = int(choice)
            selected_item = list[Category][item_choice - 1]
            selected_price = Price[Category][item_choice -1]

            cart.append((selected_item,selected_price))

            print(f"Added: {selected_item} - {selected_price}")
# Ask for another category 
    another_category = input("\nDo you want to choose another category? (yes/no): ").strip().lower()
    if another_category == "no":
        break
# Cart mein add
print("\n==========CART==========")
for item, price in cart:
     print(f"{item} - {price}")
total_price = sum(price for item,price in cart)
print(f"\ntotal cart price: {total_price}")
print("Thank you for shopping!")