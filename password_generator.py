import random
import string
#strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "01234567890"
symbols = "!@#$%^&*()?"

def split(word):
    return [char for char in word]

s = split(s)
lower_case = split(lower_case)
upper_case = split(upper_case)
numbers = split(numbers)
symbols = split(symbols)

#8: 2, 2, 2, 2
#9: 3, 2, 2, 2
#10: 4, 2, 2, 2
#11: 5, 2, 2, 2
#12: 6, 2, 2, 2
#13: 7, 2, 2, 2
#14 8, 2, 2, 2

# print("Welcome to password generator! ")
# pw_length = int(input("Now accepting length... Enter a number between 8 and 14: "))
pw_length = 5
password = ['*']*pw_length

# upper case
for a in range(0, 2):
    password[a] = upper_case[random.randint(1,(len(upper_case)-1))]

# number
for b in range(2, 4):
    password[b] = numbers[random.randint(1,(len(numbers))-1)]

# symbols
for c in range(4, 6):
    password[c] = symbols[random.randint(1,(len(symbols))-1)]

# lower case
for d in range(6, pw_length):
    password[d] = lower_case[random.randint(1,(len(lower_case))-1)]

password = list(password)

print(password)
