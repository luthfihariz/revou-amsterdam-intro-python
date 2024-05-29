# x = 25
# y = 20

# if x < 15:
#     print("x is less than 15")

# if x > 15:
#     print("x is greater than 15")

# if x == y:
#     print("x is equal to y")

# if x != y:
#     print("x is not equal to y")


# a, b = True, False

# if a and b:
#     print("a and b both are True")

# if a or b:
#     print("a or b is True")

# if not a:
#     print("a is False")

# if a is True:
#     print("a is True")

# a = None
# if a:
#     print("a is also True")

# c = 15
# if (a and b) or c > 10:
#     print("a and b are both True or c is greater than 10")


country = "UK"
match country:
    case "ID":
        print("Indonesia")
    case "SG":
        print("Singapore")
    case "MY":
        print("Malaysia")
    case _:
        print("Unknown")