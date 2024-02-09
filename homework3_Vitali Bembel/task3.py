def tuple_practice(arraycoreteg):
    coreteg = tuple(arraycoreteg)
    listn = list(arraycoreteg)
    cortegeList = list(arraycoreteg)
    a = []

    if arraycoreteg == listn:
        for i, v in enumerate(coreteg):
            a.append(i+1)
            if v == 'a':
                v = 'a'
                cortegeList[i] = v
            if v == 'b':
                v = 2
                cortegeList[i] = v
            if v == 'c':
                v = 'python'
                cortegeList[i] = v

        return tuple(cortegeList), a
    if arraycoreteg == coreteg:
        return listn
    # return (coreteg, listn)

a = ['a', 'b', 'c']
b = ('a', 'b', 'c')
print(tuple_practice(a))
print(tuple_practice(b))