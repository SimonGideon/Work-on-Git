supermarket = {
    "Sugar": 110,
    "Flour": 250,
    "Rice": 200,
    "Blue_band": 300
}

cart = {}
print("Type exit to finish customer order.....")
while True:
    product = input("Enter the product: ")
    product = product.title()
    if product in supermarket:
        quantity = input("Enter Quantity: ")
        quantity = int(quantity)
        if type(quantity) == int:
            cart[product] = quantity
        else:
            print("Invalid Quantity")
    elif product == "Exit":
        totalPrice = 0
        for key, value in cart.items():
            price = supermarket[key] * cart[key]
            totalPrice += price
            print(f"{key},{cart[key]} kgs, {supermarket[key]} (perUnit)----> {price}")
        print(f"Total Price: {totalPrice}")
        break
    else:
        
        print("Invalid Product........")
