#Exercise 1: Create a dictionary from two lists using the zip function


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = dict(zip(keys, values))
print(result)


 #Exercise 2 Cinemax
def ticket_price(age):
    if age < 3:
        return 0
    elif age <= 12:
        return 10
    else:
        return 15
    
family= {"Rolf": 43, "beth": 13, "morty": 5, "summer": 8}
total_cost = 0
for name, age in family.items():
        total_cost += ticket_price(age)
        print(f"{name} has to pay {ticket_price(age)} dollars.")
print(f"The total cost for the family is: {total_cost}")

    #Allowing user to input their own family members and ages
user_family = {}
while True:
        name = input("name: ").strip()
        if not name:
            break
        age = int(input("age: ").strip())
        if not age.isdigit():
         print("Please Enter a Valid age")
        continue
user_family[name] = int(age)
total_cost = 0
for name, age in user_family.items():
        price = ticket_price(age)
        total_cost += price 
        print(f"{name} has to pay {price} dollars.")
print(f"The total cost for the family is: {total_cost}")


    #Exercise 3

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"],
    },
}

# Modify number_stores
brand["number_stores"] = 2

# Print sentence describing Zara's clients
print(f"Zara's clients are {', '.join(brand['type_of_clothes'])}.")

# Add country_creation
brand["country_creation"] = "Spain"

# Add Desigual to international competitors if key exists
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# Delete creation_date
brand.pop("creation_date", None)

# Print the last international competitor
print(brand["international_competitors"][-1])

# Print US major colors
print(brand["major_color"]["US"])

# Print number of keys
print(len(brand))

# Print all keys
print(list(brand.keys()))

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 2,
}

# Merge dictionaries and print result
brand.update(more_on_zara)
print(brand)
    
#Exercice 4

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")


#Exercice 5

import random

def compare_number(user_number):
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print("Success!") 
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")

compare_number(50)

#Exercice 6

def make_shirt(size="Large",text="I love Python"):
    print(f"The shirt size is {size} and the text is {text}.")
    
make_shirt("large", "i love python")
make_shirt("medium", "i love python")
make_shirt("small", "i love python")

    
# Exercise 7: Temperature Advice

#Write a function that generates a random temperature between -10 and 40 degrees Celsius.
import random


def get_random_temp(use_float=False, month=None):
    
    low, high = -10, 40
    if month is not None:
        try:
            m = int(month)
        except (TypeError, ValueError):
            m = None

        if m in (12, 1, 2):
            low, high = -10, 7    # winter
        elif m in (3, 4, 5):
            low, high = 0, 16     # spring
        elif m in (6, 7, 8):
            low, high = 16, 40    # summer
        elif m in (9, 10, 11):
            low, high = 0, 25     # autumn

    if use_float:
        return random.uniform(low, high)
    return random.randint(int(low), int(high))


def main():
    prompt = (
        "Press Enter for default integer temp, 'f' for float,\n"
        "or enter a month number (1-12) to get a season-based temp: "
    )
    choice = input(prompt).strip()

    month = None
    use_float = False
    if choice.lower() == 'f':
        use_float = True
    elif choice.isdigit():
        m = int(choice)
        if 1 <= m <= 12:
            month = m
            use_float = True

    temp = get_random_temp(use_float=use_float, month=month)

    # Format temperature for display
    if isinstance(temp, float):
        temp_str = f"{temp:.1f}"
    else:
        temp_str = str(temp)

    print(f"The temperature right now is {temp_str} degrees Celsius.")

    # Use numeric value for comparisons
    t = float(temp)

    if t < 0:
        advice = "Brrr, that’s freezing! Wear some extra layers today."
    elif 0 <= t <= 16:
        advice = "Quite chilly! Don't forget your coat."
    elif 16 < t <= 23:
        advice = "Nice weather."
    elif 23 < t <= 32:
        advice = "A bit warm, stay hydrated."
    else:
        advice = "It's really hot! Stay cool."

    print(advice)


if __name__ == '__main__':
    main()


#Exercice 8

pizza_toppings = []
base_price = 10.00
topping_price = 2.50

while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ").strip()
    if topping.lower() == 'quit':
        break
    if topping:
        pizza_toppings.append(topping)
        print(f"Adding {topping} to your pizza.")

print("\nYour pizza toppings:")
if pizza_toppings:
    for topping in pizza_toppings:
        print(f"- {topping}")
else:
    print("- No toppings added")

total_cost = base_price + topping_price * len(pizza_toppings)
print(f"\nTotal cost: ${total_cost:.2f}")

