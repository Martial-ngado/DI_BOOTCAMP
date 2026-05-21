#Exercice 1
 
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3
    return oldest


cat1 = Cat("Whiskers", 3)
cat2 = Cat("Mittens", 5)
cat3 = Cat("Shadow", 4)

oldest = oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")
 


#Exercise 2: Create a class called Dog with attributes name and height, 
# and methods bark and jump. 
# The bark method should print the dog's name followed by "goes woof!",
#  and the jump method should print the dog's name followed by "jumps" and the height of the jump (which is double the dog's height). 
# Then create two instances of the Dog class, print their names and heights,
# call their bark and jump methods, and finally determine which dog is bigger based on their height.


 
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")


davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 30)

print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is bigger.")
else:
    print(f"{davids_dog.name} and {sarahs_dog.name} are the same size.")
 


#Exercise 3: Create a class called Song, it will have an attribute called lyrics.
#The lyrics attribute should be a list of strings.
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

stairway.sing_me_a_song()

#Exercise 4: Create a class called Zoo, it will have a name and an animals attribute which is a list of animals in the zoo.
#The Zoo class will also have three methods: add_animal, get_animals, and sell_animal. The add_animal method will add an animal to the animals list,
#the get_animals method will print all the animals in the zoo, and the sell_animal method will remove an animal from the animals list.

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self._groups = {}

    def add_animal(self, *new_animals):
        for new_animal in new_animals:
            if new_animal not in self.animals:
                self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        groups = {}
        for animal in self.animals:
            letter = animal[0].upper()
            groups.setdefault(letter, []).append(animal)
        self._groups = groups
        return groups

    def get_groups(self):
        if not self._groups:
            self.sort_animals()
        for letter, animals in self._groups.items():
            print(f"{letter}: {animals}")


brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Lion", "Zebra", "Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
