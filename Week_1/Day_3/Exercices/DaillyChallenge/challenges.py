class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type=None, count=1, **animals):
        if animal_type:
            self.animals[animal_type] = self.animals.get(animal_type, 0) + count

        for animal_name, quantity in animals.items():
            self.animals[animal_name] = self.animals.get(animal_name, 0) + quantity

    def get_info(self):
        lines = [f"{self.name}'s farm", ""]
        for animal_type, count in self.animals.items():
            lines.append(f"{animal_type} : {count}")
        lines.append("")
        lines.append("    E-I-E-I-0!")
        return "\n".join(lines)

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        types = self.get_animal_types()
        animal_names = []
        for animal in types:
            count = self.animals.get(animal, 0)
            name = animal + "s" if count > 1 else animal
            animal_names.append(name)

        if len(animal_names) == 0:
            animal_list = ""
        elif len(animal_names) == 1:
            animal_list = animal_names[0]
        else:
            animal_list = ", ".join(animal_names[:-1]) + " and " + animal_names[-1]

        return f"{self.name}'s farm has {animal_list}."


if __name__ == "__main__":
    macdonald = Farm("McDonald")
    macdonald.add_animal('cow', 5)
    macdonald.add_animal('sheep')
    macdonald.add_animal('sheep')
    macdonald.add_animal('goat', 12)
    print(macdonald.get_info())
    print()
    print(macdonald.get_short_info())

    bonus_farm = Farm("Old MacDonald")
    bonus_farm.add_animal(cow=2, pig=3, horse=1)
    print()
    print(bonus_farm.get_info())
    print(bonus_farm.get_short_info())
