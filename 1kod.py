import random
import string

print("Hello. I'm a password generator. Please type how long should be your password.")
x = int(input("Enter a number >>> "))

password = []

characters = string.ascii_letters + string.digits + string.punctuation

for _ in range(x):
    y = random.choice(characters)
    password.append(y)

print("Generated password:", ''.join(password))
