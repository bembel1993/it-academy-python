#enterString = str(input("Введите строку:\n "))
inputstring = "abc cde def"

newstringarr = ""

for x in inputstring:
    if x not in newstringarr and x != " ":
        newstringarr += x

print(newstringarr)