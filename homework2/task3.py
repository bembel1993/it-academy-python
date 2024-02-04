import re
import string

#enterString = str(input("Введите строку:\n "))
enterString = "abc cde def"
arrStr = enterString.replace(" ", "")

print(arrStr)

newStringArr = []

for x in arrStr:
    if x not in newStringArr:
        newStringArr.append(x)
        
newStr = ''.join(newStringArr)
print(newStr)