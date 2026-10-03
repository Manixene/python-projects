products =[
     [ "Laptop", "Smartphone", "Headphones", "Camera"],
     [" Shirts", " Pants", "Jacket","Baggy Jeans", "Cargo", "T-Shirts", "Formal Pants"],
     [" Fiction", "Non -Fiction", "Textbooks", "Self- Improvement", "Business", "Magazines"],
     ["Blender", "Microwave", "Coffee Maker", "Toaster", "Kettle"]
]
Prices = [
    [ 100000, 50000, 300000,150000,80000],
    [2000,2500,3000,1500,1800,1200,2200],
    [ 500,700,1000,800,600,400],
    [10000,15000,8000,5000,6000]
]
Categories = ["Electronics", "Clothes", "Books", "Home & Kitchen"]


Catalog = {
    "Products":products,
    "Prices": Prices,
    "Categories": Categories
}

Cart = []
while True:
    print("\n=====PRODUCT CATALOG======")
    print("Available Categories")
    for i, category in enumerate(Catalog["Categories"]):
        print(f"{i + 1}.{category}")
    print("5.Exit")

    choice = input("Choose a category: ")
    if not choice.isdigit():
        print("Please enter a number.")
        continue
    choice = int(choice)
    if choice == 5:
        break

    if choice < 1 or choice > 4:
        print("Invalid Category")
        continue

    #------Category select-------
    category_index = choice - 1
    selected_category = Catalog["Categories"][category_index]
    selected_products = Catalog["Products"][category_index]
    selected_prices = Catalog["Prices"][category_index]
    print(f"\n======{selected_category}======")

    # -----------Budget Question-----------
    filter_choice = input("\nDo you want to filter products by your budget?(yes/no): ").strip().lower()
    available_products = []
    #-----IF YES------
    if filter_choice == "yes":
        budget = int(input("Enter your maximum budget: "))
        for i, product in enumerate(selected_products):
            if selected_prices[i] <= budget:
                available_products.append((product,selected_prices[i]))
#---------IF NO---------
    else:
        for i, product in enumerate(selected_products):
            available_products.append((product,selected_prices[i]))
    #---------SHOW PRODUCTS---------
    if len(available_products) == 0:
        print("\nNo products found.")
        continue
    print("\nAvailable products: ")
    for i, item in enumerate(available_products):
        print(f"{i + 1}.{item[0]} -{item[1]}")
    #---------SELECT PRODUCTS----------
    products_choices = input("/nChoose product numbers ( example: 1 2 3):").split()

    selected_items = []

    for number in products_choices:
        if number.isdigit():
            index = int(number) - 1
            if 0 <= index < len(available_products):
                product= available_products[index][0]
                price= available_products[index][1]

                Cart.append((selected_category,product,price))
                selected_items.append((product,price))
            else:
                print("Invalid input:",number)

    #---------------SHOW SELECTION---------------------
        if len(selected_items)> 0:
            print("\n=========YOUR SELECTION==========")
            for product,prices in selected_items:
                print(f"{product}-{prices}")

    # ------------ANOTHER CATEGORY------------
        again = input("\nDo you want to explore another category ? (yes/no):").strip().lower()
        if again!= "yes":
            break
#----------Final Cart-----------
print("\n=========YOUR CART=========")
if len(Cart) == 0:
    print("Your cart is empty.")
else:
    total= 0
    for category,product,price in Cart:
        print(f"{product}{category}{price}")
        total = total + price
    print("------------------------------")
    print(f"Total Cart Value:{total}")

print("\nThank you for using Product catalog!")
  




