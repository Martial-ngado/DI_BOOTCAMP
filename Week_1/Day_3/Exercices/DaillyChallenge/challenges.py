# Define a class called Farm to represent a farm with animals
class Farm:

    # Constructor method — runs automatically when a Farm object is created
    def __init__(self, farm_name):
        self.name = farm_name  # Store the farm's name as an instance attribute
        self.animals = {}      # Initialize an empty dictionary to hold animal types and their counts

    # Method to add animals to the farm
    # Accepts an optional positional animal_type with a count, OR keyword arguments for multiple animals at once
    def add_animal(self, animal_type=None, count=1, **animals):
        if animal_type:  # If a single animal_type string was provided...
            # Add 'count' to the existing count for that animal (default to 0 if not yet tracked)
            self.animals[animal_type] = self.animals.get(animal_type, 0) + count

        # Loop through any keyword arguments (e.g. cow=2, pig=3)
        for animal_name, quantity in animals.items():
            # Add the given quantity to the existing count for each animal keyword
            self.animals[animal_name] = self.animals.get(animal_name, 0) + quantity

    # Method to return a detailed, formatted string about the farm and all its animals
    def get_info(self):
        lines = [f"{self.name}'s farm", ""]  # Start with the farm name and a blank line
        for animal_type, count in self.animals.items():  # Loop through each animal and its count
            lines.append(f"{animal_type} : {count}")    # Add a line like "cow : 5"
        lines.append("")                    # Add a blank line at the end
        lines.append("    E-I-E-I-0!")     # Add the classic Old MacDonald sign-off
        return "\n".join(lines)            # Join all lines with newlines and return as one string

    # Method to return a sorted list of animal type names (keys from the animals dictionary)
    def get_animal_types(self):
        return sorted(self.animals.keys())  # Sort alphabetically and return

    # Method to return a short, human-readable summary of what animals the farm has
    def get_short_info(self):
        types = self.get_animal_types()  # Get the sorted list of animal types
        animal_names = []                # List to hold pluralized (or singular) animal names

        for animal in types:
            count = self.animals.get(animal, 0)          # Get the count for this animal
            name = animal + "s" if count > 1 else animal # Pluralize the name if count > 1
            animal_names.append(name)                    # Add to the list

        # Build the animal list string depending on how many types there are
        if len(animal_names) == 0:
            animal_list = ""                                                    # No animals: empty string
        elif len(animal_names) == 1:
            animal_list = animal_names[0]                                       # One animal: just its name
        else:
            # Multiple animals: join all but the last with ", ", then add "and" before the last
            animal_list = ", ".join(animal_names[:-1]) + " and " + animal_names[-1]

        return f"{self.name}'s farm has {animal_list}."  # Return the final summary sentence


# Entry point — this block only runs when the script is executed directly (not imported)
if __name__ == "__main__":
    macdonald = Farm("McDonald")   # Create a Farm named "McDonald"
    macdonald.add_animal('cow', 5) # Add 5 cows
    macdonald.add_animal('sheep')  # Add 1 sheep (count defaults to 1)
    macdonald.add_animal('sheep')  # Add another sheep (now 2 total)
    macdonald.add_animal('goat', 12)         # Add 12 goats
    print(macdonald.get_info())              # Print the full farm info
    print()                                  # Print a blank line
    print(macdonald.get_short_info())        # Print the short summary

    bonus_farm = Farm("Old MacDonald")            # Create a second Farm named "Old MacDonald"
    bonus_farm.add_animal(cow=2, pig=3, horse=1)  # Add multiple animals using keyword arguments
    print()
    print(bonus_farm.get_info())       # Print the full info for the bonus farm
    print(bonus_farm.get_short_info()) # Print the short summary for the bonus farm