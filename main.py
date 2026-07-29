import random
import string
print("Welcome to the password generator")
length = int(input("How long should the password be? "))
numbers=input("Do you need a numbers in your password?(yes/no):")
symbols=input("Do you need special symbols in your password? (yes/no):")
characters = string.ascii_letters

if numbers == "yes":
    characters += string.digits

if symbols == "yes":
    characters += string.punctuation
password = "".join(random.choices(characters, k=length))
print("Your password is:", password)


