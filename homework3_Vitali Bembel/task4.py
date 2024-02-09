def similarnumber(num):
    num = num.split()
    b = []
    c = []
    d = []
    sum = 0
    for i, v in enumerate(num):
        b.append(i+1)
        c.append(v)
        for i2 in range(i+1, len(num)):
            if v == num[i2]:
                d.append(v)
                sum += 1
    return b, c, d, sum

a = "1 2 3 4 2 2 1 3 4 5 6"

print(similarnumber(a))
