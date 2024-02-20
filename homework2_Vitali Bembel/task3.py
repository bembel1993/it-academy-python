#input_string = str(input("Введите строку:\n "))
input_string = "abc cde def"

new_string_arr = ""

for x in input_string:
    if x not in new_string_arr and x != " ":
        new_string_arr += x

print(new_string_arr)