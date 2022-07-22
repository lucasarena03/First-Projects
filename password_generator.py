#must have letters, numbers, and symbols
#ask how long the password is
#print out password with right lenght on screen
#if they enter for a negative number or password less than 1 letter say theyre stupid

import string
import random
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def generate_random_password():
    length = int(input("Enter password length: "))
    random.shuffle(characters)
    password = []
    if length < 1:
        print("stupid idiot")
        return
    for _i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    print("".join(password))

generate_random_password()