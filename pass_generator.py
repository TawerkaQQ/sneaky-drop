import string
import secrets
import random
# import pyperclip


def generator(len):
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    all = upper+lower+digits+punctuation

    password_len = len
    part1 = round(password_len * (30 / 100))#letters %60
    part2 = round(password_len * (20 / 100))#digits+punc %40

    password=""
    for i in range(part1):
        password += secrets.choice(upper)
        password += secrets.choice(digits)

    for i in range(part2):
        password += secrets.choice(punctuation)
        password += secrets.choice(lower)
    return password
