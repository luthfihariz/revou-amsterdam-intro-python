# inheritance
# base class / parent class


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says something")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")


dog = Dog("Buddy")
dog.speak()

cat = Cat("Whiskers")
cat.speak()


# Multiple inheritance
class Character:
    def __init__(self, name):
        self.name = name


class Walker:
    def walk(self):
        print(f"{self.name} is walking.")


class Swimmer:
    def swim(self):
        print(f"{self.name} is swimming.")


class Flying:
    def fly(self):
        print(f"{self.name} is flying.")


class SuperCharacter(Walker, Swimmer, Flying, Character):
    def __init__(self, name):
        super().__init__(name)


class WalkingCharacter(Walker, Character):
    def __init__(self, name):
        super().__init__(name)


# Create an instance of GameCharacter
hero = SuperCharacter("Hero")

# Call methods from multiple parent classes
hero.walk()  # Prints: Hero is walking.
hero.swim()  # Prints: Hero is swimming.
hero.fly()  # Prints: Hero is flying.
