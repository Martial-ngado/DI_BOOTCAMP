# ============================================================
# CHALLENGE 1 - Multiples list
# ============================================================
number = int(input("Enter a number: "))
length = int(input("Enter the length of the list: "))

multiples = []

for i in range(1, length + 1):
    multiples.append(number * i)

print(multiples)


# ============================================================
# CHALLENGE 2 - Remove consecutive duplicate characters
# ============================================================
text = input("Enter a string: ")

result = text[0]

for char in text[1:]:
    if char != result[-1]:
        result += char

print("New string:", result)
