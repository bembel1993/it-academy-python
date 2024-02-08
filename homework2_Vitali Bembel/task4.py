import re
import string

#enterString = str(input("Введите строку:\n "))
enterString = "aBjksdjskdKJHKJHUTFlmlmAc"
spt = []

for x in enterString:
    spt.append(x)

UpperQty = 0
LowerQty = 0

for x in range(len(spt)):
    if spt[x].isupper():
        UpperQty += 1
    if spt[x].islower():
        LowerQty += 1

print("Строчных букв: " + str(LowerQty) + "\nПрописных букв: " + str(UpperQty))
        



