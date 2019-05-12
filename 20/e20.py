#!/usr/bin/env python3

##################
# Element Search #
##################

import math

def simple_search(_list, _elem):
    for i in _list:
        if   _elem == i: return True
        elif _elem <  i: return False
    return False

def binary_search(_list,_elem):
    fst_index = 0               # first possible index with _elem
    lst_index = len(_list)-1    # last  possible index with _elem

    while fst_index <= lst_index:
        mid_index = math.floor(  fst_index + (lst_index-fst_index)/2  )
        if   _elem > _list[mid_index]: fst_index = mid_index+1
        elif _elem < _list[mid_index]: lst_index = mid_index-1
        else:
            return True
    return False

def binary_search2(_list,_elem):
    while _list != []:
        mid = math.floor(len(_list)/2)
        if   _elem < _list[mid]: _list = _list[     :mid]
        elif _elem > _list[mid]: _list = _list[mid+1:   ]
        else:
            return True
    return False


if __name__=="__main__":
    a = [0,3,6,7,9,11,14,21,22,25]

    print("lista =",a,"\n")
    print("Elem\t",   "simple\t",              "binary\t",             "binary2")
    for i in range(-1,27):
        print(i,":\t", simple_search(a,i),"\t", binary_search(a,i),"\t",binary_search2(a,i))

