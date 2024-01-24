# 아래 함수를 수정하시오.
def remove_duplicates(args):
    new_lst = []
    # 1번째 방법
    new_lst = list(set(args))
    return new_lst

def remove_duplicates2(args):
    new_lst = []
    # 2번째 방법
    for i in args:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst
result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
result2 = remove_duplicates2([1, 2, 2, 3, 4, 4, 5])
print(result2)