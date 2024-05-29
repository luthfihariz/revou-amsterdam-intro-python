foods = ["Sate", "Burger", "Pizza", "Pecel Lele", "Bakso", "Sushi"]

print(foods[3])

foods.append("Sushi")

print(foods)

foods.insert(2, "Noodle")

print(foods)

try:
    foods.remove("Bakso")
except ValueError:
    print("item is not in the list")

print(foods)

# print(len(foods))

#print(foods.index("Sushi"))

if "Sateee" in foods:
    foods.remove("Sate")
else:
    print("Sateee is not in the list")

print(foods)


# Slicing
# list[start:stop:step]
# list[start:stop]
# list[start:]
# list[:stop]
# list[start::step]


print(foods)

print(foods[0:5:2])

print(foods[2::2])

foods.extend(["Mie Ayam", "Rujak"])
print(foods)

foods["Mie Ayam"]
print(foods)