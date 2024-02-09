# 2.	List practice
# 1.	Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# 2.	Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
# 3.	Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
# 4.	Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
# 5.	Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.


def list_practice(list):
    b = list
    c = []
    for x in range(len(list)):
        if x % 2 == 0:
            c.append(list[x])

    return ("1.", b, "2.", c)

def list_practice2(list):
    b = list
    c = []
    d = b.copy()
    e = d.copy()
    for x in range(len(list)):
        if x == 1:
            c = b.pop(x)
            e.append(c)
    return ("3.", d, "4", c, "5.", e)

a = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
b = ['1a', '2a', '3a', '4a']


print(list_practice(a))
print(list_practice2(b))

