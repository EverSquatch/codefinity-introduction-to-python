produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = []
groceries.append(produce)
groceries.append(dairy)
#groceries = [produce] + [dairy]

for section in groceries:
    for item in section:
        print("Item name: ", item)