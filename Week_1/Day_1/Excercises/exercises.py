
#Exercice 1 "Hello World"
print("Hello Word\n" *4)


#Exercice 2 "Raise to Power"
print(99**3*8)

#Exercice 3 "Comparing"
15 < 8 #False
#this is false because 15 is greater than 
5 < 3 #false because 5 is greater than 3
3 == 3 #true because 3 is equal to 3
3 == "3" #false because 3 is an integer and "3" is a string
"3" > 3 #false because "3" is a string and 3 is an integer
"Hello" == "hello" #false because of case sensitivity


#Exercice 4 computer and brand
computer_brand = "Dell"
print("I have a " + computer_brand + " computer.")


#Exercice 5 Infos about me 
name = "Martial N'GADO"
age = 26
shoe_size = 44
info = "Call me the great " + name + ", I am " + str(age) + " years old and my shoe size is " + str(shoe_size) + "."
print(info)

#Exercice 6 simple if condition
a = 9
b = 8
if a > b:
    print("Hello World")


#Exercice 7 Even or Odd
number = int(input("Enter a number: ")) #function input : to allow user to type from the keyboard
if number % 2 ==0: # % uses modulo if the reste of division of the number input by 2 is 0 then it is an even num
     print("Even")
else :
     print("Odd")




#Exercice 8 name comparison
my_name = "Martial"
user_name = input("What is your name")
if user_name == my_name:
        print("Hey buddy, we have the same name😂😂")
else :
        print("oops, i thought we had the same name😂😂, sorry oo")




#Exercice 9 checking the height

height = int(input("Enter your height in cm:  "))
if height > 145:
        print("You are tall enough to ride")
else :
        print("You need to grow some more to ride")

