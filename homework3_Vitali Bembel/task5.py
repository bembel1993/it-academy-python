# 5.	Уникальные элементы в списке
# Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить
# в том порядке, в котором они встречаются в списке


def unique_elements(uniq):
    listn = uniq
    uniq_list = []
    for i, v in enumerate(listn):
        if listn.count(v) <= 1 and v not in uniq_list:
            uniq_list.append(v)
    return uniq_list

a = [1, 2, 2, 3, "a", "b", "a", "abc", 3, "b"]
print(unique_elements(a))