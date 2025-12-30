meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]


deli_dept = [meat, cheese, condiment]
print("Initial Deli List: ", deli_dept)

if "Ham" in deli_dept[0] and deli_dept[0][2] < 100:
    deli_dept[0][2] = 100

deli_dept.append(seasonal_meat)
deli_dept.remove(condiment)
deli_dept.sort()

print("Updated Deli List: ", deli_dept)
    