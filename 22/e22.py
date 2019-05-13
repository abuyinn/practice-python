#!/usr/bin/env python3

def count_from_list(_list):
    dictionary = {}
    for e in _list:
        if e in dictionary.keys(): dictionary[e]+= 1
        else:                      dictionary[e] = 1
    return dictionary
 
def print_times(dictionary):
    for e in dictionary.items():
        print(e[0],"is",e[1],"times.")


if __name__ == "__main__":
    filename1 = "nameslist.txt"
    filename2 = "Training_01.txt"

    with open(filename1, 'r') as file1:
        names = file1.read().split("\n")
        dict1 = count_from_list(names)
        print_times(dict1)

    with open(filename2,'r') as file2:
        lines = file2.read().split("\n")[:-1]
        categories = []
        for line in lines:
            cat = line[3:]
            cat = cat[:cat.index('/')]
            categories.append(cat)
        dict2 = count_from_list(categories)
        print_times(dict2)

