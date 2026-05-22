import random
from Exercices import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        names = [self.name]
        for a in args:
            names.append(getattr(a, 'name', str(a)))
        print(f"{', '.join(names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead",
            ]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet")


# Test PetDog methods
if __name__ == "__main__":
    fido = PetDog("Fido", 2, 10)
    buddy = PetDog("Buddy", 3, 12)
    max_dog = PetDog("Max", 4, 15)

    fido.train()
    fido.play(buddy, max_dog)
    fido.do_a_trick()

    buddy.do_a_trick()
    buddy.train()
    buddy.do_a_trick()
