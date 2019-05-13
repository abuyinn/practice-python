#!/usr/bin/env python3

def file2list(filename):
    with open(filename, 'r') as f:
        return f.read().split("\n")

def overlapping_fast(_list1, _list2):
    overlap = []
    i1 = 0          # index of the element on _list1
    i2 = 0          # index of the element on _list2
    len1=len(_list1)
    len2=len(_list2)
    while i1<len1 and i2<len2:
        if _list1[i1] == _list2[i2]:
            overlap.append(_list1[i1])
            i1+=1
            i2+=1
        elif _list1[i1] < _list2[i2]:
            i1+=1
        else:
            i2+=1
    return overlap

def overlapping_short(_list1, _list2):
    return [e for e in _list1 if e in _list2]

if __name__=="__main__":
    filename_prime = "primenumbers.txt"
    filename_happy = "happynumbers.txt"
    
    list_prime = file2list(filename_prime)
    list_happy = file2list(filename_happy)

    overlap_fast  = overlapping_fast (list_prime, list_happy)
    overlap_short = overlapping_short(list_prime, list_happy)

    print("Overlap_fast:\n", overlap_fast,'\n', sep='')
    print("Overlap_short is the same:",overlap_fast==overlap_short)

