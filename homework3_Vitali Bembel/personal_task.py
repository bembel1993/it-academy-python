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