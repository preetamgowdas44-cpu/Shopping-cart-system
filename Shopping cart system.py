products={
    "Apple":50,
    "Bannana":25,
    "Mango":80,
    "Bread":50,
    "Calculator":1400
}

cart=[]

def view_products():
    print("\n---Availble Items---")
    for product,amount in products.items():
        print(f"{product} - ₹{amount}")
    print()

def add_to_cart():
    product=input("\nEnter the product name tht you want to add:- ").capitalize()
    if product in products:
        cart.append(product)
        print(f"{product} added to cart sucessfully.")
    else:
        print("Invalid input! Item not found.")

def remove_from_cart():
    product=input("\nEnter the product name that you want to remove:- ").capitalize()
    if product in products:
        cart.remove(product)
        print(f"{product} removed from cart sucessfully.")
    else:
        print("Invalid input! Item not found.")

def view_cart():
    if not cart:
        print("No items found in your cart!")
    else:
        print("\n---Items in your cart---")
        total=0
        for product in cart:
            print(f"{product} - {products[product]}")
            total+=products[product]
        print(f"Total = ₹{total}")

def chekout():
    if not cart:
        print("No items found in your cart!")
    else:
        print("\n---Items in your cart---")
        total=0
        for product in cart:
            print(f"{product} - {products[product]}")
            total+=products[product]
        print(f"Total = ₹{total}")
        print("Thankyou for shopping!")
        cart.clear()

def menu():
    while True:
        print("\n-----Main Menu-----")
        print("1.View Products.")
        print("2.Add items to the cart.")
        print("3.Remove item from the cart.")
        print("4.View Cart.")
        print("5.Checkout.")

        try:
            choice=int(input("Enter your choice:- "))
        except ValueError:
            print("Invalid input! Please enter a number between (1-4)")
            continue

        if choice==1:
            view_products()
        elif choice==2:
            add_to_cart()
        elif choice==3:
            remove_from_cart()
        elif choice==4:
            view_cart()
        elif choice==5:
            chekout()
            break
        else:
            print("Invalid choice!.Try again")

menu()