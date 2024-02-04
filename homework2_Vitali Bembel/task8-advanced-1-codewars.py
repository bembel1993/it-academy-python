import re
import string

# Test Advanced from codewars.com

# Your task is to write a function maskify, 
# which changes all but the last four characters into '#'.

def maskify(cc):
    if len(enterNumber) > 16:
        print("Введенный номер больше 16")
    elif len(enterNumber) < 16:
        print("Введенный номер меньше 16")
    elif len(enterNumber) == 16:
        last4Number = re.search('[0-9]{4}$', enterNumber)
        first12Number = re.search(r'^[0-9]{12}', enterNumber)
        hiddenNum = "#" * len(first12Number.group())
        newStr = hiddenNum+""+str(last4Number.group())
        print ("\"" + enterNumber + "\"" + " --> " + newStr)

#enterNumber = input("Введите номер карты (16-значный номер):\n ")
enterNumber = "4556364607935616"

maskify(enterNumber)