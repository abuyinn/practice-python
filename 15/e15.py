def strange_rev(_str):
    list_of_str     = _str.split(" ")
    rev_list_of_str = list_of_str[::-1]
    return " ".join(rev_list_of_str)

s = input("Give a string with spaces: ")

print(strange_rev(s))

