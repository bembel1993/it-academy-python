def unique_elements(uniq):
    listn = uniq
    uniqList = []
    for i, v in enumerate(listn):
        if listn.count(v) <= 1 and v not in uniqList:
            uniqList.append(v)
    return uniqList

a = [1, 2, 2, 3, "a", "b", "a", "abc", 3, "b"]
print(unique_elements(a))