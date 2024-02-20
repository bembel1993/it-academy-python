# 3.	Tuple practice
# 1.	Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
# 2.	Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
# 3.	Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
# 4.	Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы последовательно выводились
# значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.


def tuple_practice(arraycoreteg):
    coreteg = tuple(arraycoreteg)
    listn = list(arraycoreteg)
    cortegeList = list(arraycoreteg)
    a = []

    if arraycoreteg == listn:
        for i, v in enumerate(coreteg):
            a.append(i+1)
            if v == 'a':
                v = 'a'
                cortegeList[i] = v
            if v == 'b':
                v = 2
                cortegeList[i] = v
            if v == 'c':
                v = 'python'
                cortegeList[i] = v

        return tuple(cortegeList), a
    if arraycoreteg == coreteg:
        return listn

a_list = ['a', 'b', 'c']
b_coreteg = ('a', 'b', 'c')
print(tuple_practice(a_list))
print(tuple_practice(b_coreteg))