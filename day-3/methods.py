# Instance methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

    def birthday(self):
        self.age += 1

    # class method
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2024 - birth_year)

    # dunder methods
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __eq__(self, other): # Introduce variable ktp_number
        return self.name == other.name and self.age == other.age


class PersonUtil:
    @staticmethod
    def is_adult(age):
        return age >= 18


# Creating an instance of the class
john = Person("John", 30)
john.say_hello()
john.birthday()
john.say_hello()

# Using class method
jane = Person.from_birth_year("Jane", 2015)

# Using static method
# Try for jane.is_adult() first to show an error and ask the students to debug
print(PersonUtil.is_adult(jane.age))

# Using magic methods
print(john)
print(john == jane)
