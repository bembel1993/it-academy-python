def sort_max_four_number(mylist):
    newList = []
    for i in range(len(mylist)):
        for j in range(i+1, len(mylist)):
            if mylist[i] < mylist[j]:
                tmp = mylist[i]
                mylist[i] = mylist[j]
                mylist[j] = tmp
        if i <= 4-1:
            newList.append(mylist[i])

    return newList

a = [1, 33, 5, 1, 10, 9, 234, 988, 5, 76, 0, 23]
print(sort_max_four_number(a))



def roman_to_int(roman_number):
    value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
    int_dig = []
    input_roman_dig = []
    sum_list = []
    number = 0
    for i, v in enumerate(roman_number):
        input_roman_dig.append(v)
        sum_list.append(v)
        int_dig.append(value[v])
    number = sum(int_dig)
    return input_roman_dig, number

print(roman_to_int("XXVII"))
print(roman_to_int("XXVI"))