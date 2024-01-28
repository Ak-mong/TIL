# 아래 함수를 수정하시오.
"""
def even_elements(lst):
    new_lst = []
    while lst: 
        num = lst.pop()
        if num % 2 ==0:
            new_lst.append(num)
    new_lst.reverse()
    return new_lst

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
"""
def even_elements(lst):
    new_lst = []
    while lst:
        num = lst.pop()
        if num %2 ==0:
            new_lst.extend([num])
    new_lst.reverse()
    return new_lst

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)