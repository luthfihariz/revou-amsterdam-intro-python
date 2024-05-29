animal = "cat"

if animal == "snake":
    print("This is a snake")
elif animal == "cat":
    print("This is a cat")
else:
    print("Unknown animal")


# Short hand if else
animal = "dog"
print("This is a cat") if animal == "cat" else print("This is not cat")

animal_sound = "meow" if animal == "cat" else "bark"
print(animal_sound)


animal = "butterfly"
print("This is a cat") if animal == "cat" else print("This is a dog") if animal == "dog" else print("This is not a cat or a dog.")