#enterstring = str(input("Введите строку:\n "))
enter_string = "aBjksdjskdKJHKJHUTFlmlmAc"
arr = []

for x in enter_string:
    arr.append(x)

upper_qty = 0
lower_qty = 0

for x in arr:
    if 'a' <= x <= 'z':
        upper_qty += 1
    if 'A' <= x <= 'Z':
        lower_qty += 1

print("Строчных букв: " + str(lower_qty) + "\nПрописных букв: " + str(upper_qty))
        



