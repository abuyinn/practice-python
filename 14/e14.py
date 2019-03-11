def unique_set(_list):
    return list(set(_list))

def unique_loop(_list):
    l = []
    for i in _list:
        if i not in l:
            l.append(i)
    return l

a = [1,1,2,4,6,7,9,5,3,2,6,2]
print(unique_set(a))
print(unique_loop(a))

