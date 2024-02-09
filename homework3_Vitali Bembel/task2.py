def list_practice(list):
    b = list
    c = []
    for x in range(len(list)):
        if x % 2 == 0:
            c.append(list[x])

    return ("1.", b, "2.", c)

def list_practice2(list):
    b = list
    c = []
    d = b.copy()
    e = d.copy()
    for x in range(len(list)):
        if x == 1:
            c = b.pop(x)
            e.append(c)
    return ("3.", d, "4", c, "5.", e)

a = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
b = ['1a', '2a', '3a', '4a']


print(list_practice(a))
print(list_practice2(b))

