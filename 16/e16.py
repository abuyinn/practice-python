#!/usr/bin/env python3

import string
import random

easy_chars = string.digits + string.ascii_letters
all_chars  = string.digits + string.ascii_letters + string.punctuation

def generate_passwd(_strong):
    length = _strong*_strong*2
    if strong<2:
        passwd = [random.choice(string.ascii_lowercase) for _ in range(length)]
    elif strong==2:
        passwd = [random.choice(string.ascii_letters)   for _ in range(length)]
    elif strong ==3:
        passwd = [random.choice(easy_chars)             for _ in range(length)]
    else:
        passwd = [random.choice(all_chars)              for _ in range(length)]
    return "".join(passwd)

strong = int(input("How strong the password should be? [1-4]: "))
print(generate_passwd(strong))

