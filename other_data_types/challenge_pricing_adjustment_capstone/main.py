grocery_inventory = {
    "Milk" : ("Dairy", 3.50, 8),
    "Eggs" : ("Dairy", 5.50, 30),
    "Bread" : ("Bakery", 2.99, 15),
    "Apples" : ("Produce", 1.50, 50)
}

eggs_price = grocery_inventory.get("Eggs")[1]

if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    updated_eggs_price = eggs_price - 1
    convert_grocery_to_list = list(grocery_inventory["Eggs"])
    convert_grocery_to_list[1] = updated_eggs_price
    grocery_inventory["Eggs"] = tuple(convert_grocery_to_list)
else:
    print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes" : ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes: ", grocery_inventory)

milk_stock = grocery_inventory.get("Milk")[2]

if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    increased_milk_stock = milk_stock + 20
    convert_grocery_to_list = list(grocery_inventory["Milk"])
    convert_grocery_to_list[2] = increased_milk_stock
    grocery_inventory["Milk"] = tuple(convert_grocery_to_list)
else:
    print("Milk has sufficient stock.")

apple_price = grocery_inventory.get("Apples")[1]

if apple_price > 2.0:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print("Updated inventory: ", grocery_inventory)