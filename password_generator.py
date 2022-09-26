import random
import string
def PasswordGenration(length, lower=True, upper=True, digits=True, punctuation=True):
    char = ""
    if lower:
        char += string.ascii_lowercase
    if upper:
        char += string.ascii_uppercase
    if digits:
        char += string.digits
    return ''.join(random.choice(char) for _ in range(length))
_length = int(input("How long password do you want? "))
adjust = input("Do you want to adjust the password parameters?(y/n) ")
if adjust == "y":
    _lower = input("Do you want lowercase characters?(y/n) ")
    _upper = input("Do you want uppercase characters?(y/n) ")
    _digits = input("Do you want digits?(y/n) ")
    lower = True if _lower == "y" else False
    upper = True if _upper == "y" else False
    digits = True if _digits == "y" else False
    print(PasswordGenration(_length, lower, upper, digits))
else:
    print(PasswordGenration(_length))
