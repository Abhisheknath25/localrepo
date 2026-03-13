import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if characters == "":
        print("You must select at least one character type!")
        return None

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


print("====== Advanced Password Generator ======")

length = int(input("Enter password length: "))

letters = input("Include letters? (y/n): ").lower() == "y"
numbers = input("Include numbers? (y/n): ").lower() == "y"
symbols = input("Include symbols? (y/n): ").lower() == "y"

count = int(input("How many passwords to generate?: "))

print("\nGenerated Passwords:\n")

for i in range(count):
    pwd = generate_password(length, letters, numbers, symbols)
    
    if pwd:
        if length >= 12:
            strength = "Strong"
        elif length >= 8:
            strength = "Medium"
        else:
            strength = "Weak"

        print(f"{i+1}. {pwd}  | Strength: {strength}")