def greet():
    print("Hello World")

#greet()

# function argument
def greet_personally(name):
    print(f"Selamat malam, {name}!")


# greet_personally("Rizqi Akbar")
# greet_personally(name="Beno")


# arbitrary arguments *args
def greet_many(*names):
    print(names)
    for name in names:
        print(f"Selamat belajar Python! {name}")


#greet_many("John", "Doe", "Jane", "Budi")
#greet_many("Tini")


# arbitrary keyword arguments **kwargs
def greet_custom(**greets):
    print(greets)
    for name, greeting in greets.items():
        print(f"{greeting}, {name}!")

#greet_custom(Ardi="selamat malam!", Fachmi="selamat belajar Python!")


def add_order():
    pass

#add_order()


def greet_keyword_only(*, name, greeting):
    print(f"{greeting}, {name}")

#greet_keyword_only(name="Bob", greeting="selamat malam")


#Lambda function
# def add(a, b):
#     result = a+b;
#     return result;

# print(add(5, 3))

add = lambda a, b, c, d: a + b + c + d;
print(add(10, 2))

greeting = lambda name: print(f"Hello {name}")
#greeting("Alvaro")


greet_many = lambda *names: print(names)
#greet_many("Luthfi", "Hariz")