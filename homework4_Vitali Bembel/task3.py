# 3.	Даны два списка чисел. Посчитайте, сколько различных чисел содержится одновременно как в первом списке, так и во втором

def difference_numbers_list(list1, list2):
    count = 0
    for i in list1:
        for j in list2:
            if i == j:
                count = count + 1

    return count

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

print(difference_numbers_list(list1, list2))