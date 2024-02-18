# 4.	Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один из этих списков

def uniq_number_list(list1, list2):
    uniqnum1 = []
    uniqnum2 = []
    joinlist = []
    for i in list1:
        if i not in list2:
            uniqnum1.append(i)

    for j in list2:
        if j not in list1:
            uniqnum2.append(j)

    joinlist = uniqnum1 + uniqnum2

    return len(joinlist)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

print(uniq_number_list(list1, list2))
