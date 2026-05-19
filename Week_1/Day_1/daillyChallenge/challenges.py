#Challenge 1
number = int(input("Enter a number: "))
length = int(input("Enter the length of the list: "))

multiples = []
for i in range(1, length +1):
    multiples.append(number * i)
print(multiples)




#Challenge 2 removing consecutive identical characteres
text = input("Enter a string: ")
result = text[0]
for char in text[1:]:
    if char != result[-1]:
        result += char
print("New String:", result)


