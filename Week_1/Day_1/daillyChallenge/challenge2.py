text = input("Enter a string: ")

result = text[0]

for char in text[1:]:
    if char != result[-1]:
        result += char

print("New string:", result)