#enterstring = str(input("Введите строку:\n "))
enterstring = "aBjksdjskdKJHKJHUTFlmlmAc"
arr = []

for x in enterstring:
    arr.append(x)

upperqty = 0
lowerqty = 0

for x in arr:
    if 'a' <= x <= 'z':
        upperqty += 1
    if 'A' <= x <= 'Z':
        lowerqty += 1

print("Строчных букв: " + str(lowerqty) + "\nПрописных букв: " + str(upperqty))
        



