# 아래 함수를 수정하시오.
def difference_sets(a,b):
    # return a.difference(b)
    # return a - b
    c = set()
    for i in a:
        if i not in b:
            c.add(i)
    return c


result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)
