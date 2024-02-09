def sort_list(list):
    b = []
    c = []
    d = []
    for i in range(len(list)):
        if list[i] == 0:
            b.append(list[i])
        if list[i] > 0:
            c.append(list[i])
    d = c + b
    return d

a = [0, 1, 3, 4, 0, 1, 4, 0, 0, 2]
print(sort_list(a))