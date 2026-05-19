
# EXERCISE 1 - Hello World
# ============================================================
print("Hello World!\n " * 4)


# ============================================================
# EXERCISE 2 - Power calculation
# ============================================================
print(99**3*8)


# ============================================================
# EXERCISE 3 - Comparisons
# ============================================================
15 < 8          # False — 15 is greater than 8
5 < 3           # False — 5 is greater than 3
3 == 3          # True  — 3 is equal to 3
3 == "3"        # False — 3 is an integer and "3" is a string
"3" > 3         # False — "3" is a string and 3 is an integer
"Hello" == "hello"  # False — case sensitive


# ============================================================
# EXERCISE 4 - String concatenation with a variable
# ============================================================
computer_brand = "Dell"
print("I have a " + computer_brand + " computer.")


# ============================================================
# EXERCISE 5 - Personal info string
# ============================================================
name = "Martial N'GADO"
age = 26
shoe_size = 44
info = ("Call me the great " + name + ", I am " + str(age) +
        " years old and my shoe size is " + str(shoe_size) + ".")
print(info)


# ============================================================
# EXERCISE 6 - Simple if condition
# ============================================================
a = 9
b = 8
if a > b:
    print("Hello World")


# ============================================================
# EXERCISE 7 - Even or Odd
# ============================================================
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# This program uses input() to get a number from the user,
# checks if it is even or odd using the modulus operator,
# then prints the result.


# ============================================================
# EXERCISE 8 - Name comparison
# ============================================================
my_name = "Martial"
user_name = input("What is your name? ")
if user_name == my_name:
    print("hey buddy, we have the same name😂😂😂")
else:
    print("ah ah i thought we had the same name but it seems we don't😂😂😂")



# EXERCISE 9 - Height check

height = int(input("Enter your height in cm: "))

if height > 145:
    print("You are tall enough to ride.")
else:
    print("You need to grow some more to ride.")
