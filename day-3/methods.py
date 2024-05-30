class Person:
    def __init__(self, name, age, ktp_number):
        self.name = name
        self.age = age
        self.ktp_number = ktp_number

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

    def birthday(self):
        self.age += 1

    # class method
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2024 - birth_year)
    
    # # dunder methods
    def __eq__(self, other):
        return self.ktp_number == other.ktp_number
    
    def __str__(self):
        return f"Name is {self.name}. Age is {self.age}. KTP Number is {self.ktp_number}"
        


# class PersonUtil:
#     @staticmethod
#     def is_adult(age):
#         return age >= 18
    
#     @staticmethod
#     def is_asian(race):
#         pass

# print(PersonUtil.is_adult(jane.age))
# print(PersonUtil.is_adult(john.age))

john = Person("John", 20, "123456")
john2 = Person("John", 20, "123456")

print(john)
print(john.__eq__(john2))