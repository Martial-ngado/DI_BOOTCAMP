# Exercise 1: Pets
# Key Python Topics:
# - Inheritance
# - Class instantiation
# - Lists
# - Polymorphism
"""
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Step 1: Create the Siamese class
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Step 2: Create a list of cat instances
bengal_cat = Bengal('Leo', 3)
chartreux_cat = Chartreux('Milo', 2)
siamese_cat = Siamese('Luna', 1)
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Step 3: Create a Pets instance
sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
sara_pets.walk()
"""

# Exercise 2: Dogs
# Key Python Topics:
# - Classes and objects
# - Methods
# - Attributes


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f'{self.name} won the fight'
        elif self_power < other_power:
            return f'{other_dog.name} won the fight'
        else:
            return f'{self.name} and {other_dog.name} tied'

# Step 2: Create dog instances
buddy = Dog('Buddy', 4, 25)
max_dog = Dog('Max', 3, 30)
bella = Dog('Bella', 5, 20)

# Step 3: Test dog methods
print(buddy.bark())
print(max_dog.run_speed())
print(buddy.fight(max_dog))
print(bella.fight(buddy))

class Person:
    def __init__(self, first_name: str, age: int):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self) -> bool:
        return self.age >= 18

""" Exercise 3: The Family
class Family:
    def __init__(self, last_name: str):
        self.last_name = last_name
        self.members = []

    def born(self, first_name: str, age: int):
        new_member = Person(first_name, age)
        new_member.last_name = self.last_name
        self.members.append(new_member)
        return new_member

    def check_majority(self, first_name: str):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(
                        "You are over 18, your parents Jane and John accept that you will go out with your friends"
                    )
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No family member named {first_name} was found.")

    def family_presentation(self):
        print(f"Family last name: {self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, {member.age} years old")


if __name__ == "__main__":
    simpson_family = Family("Simpson")
    simpson_family.born("Bart", 10)
    simpson_family.born("Lisa", 8)
    simpson_family.born("Maggie", 1)
    simpson_family.born("Marge", 38)

    simpson_family.family_presentation()
    print()
    simpson_family.check_majority("Bart")
    simpson_family.check_majority("Marge")
    """


