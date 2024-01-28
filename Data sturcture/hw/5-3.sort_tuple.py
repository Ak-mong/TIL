# 아래 함수를 수정하시오.
def sort_tuple(input_tuple):
    new_tuple = ()
    new_tuple = sorted(input_tuple)
    return new_tuple

result = sort_tuple((5, 2, 8, 1, 3))
print(result)

# 아래 함수를 수정하시오.
def sort_tuple2(t):
    return tuple(sorted(t))

result2 = sort_tuple((5, 2, 8, 1, 3))
print(result2)

def sort_tuple3(tup):
    a = sorted(tup)
    print(type(a))
    return tuple(a)
    pass

result3 = sort_tuple((5, 2, 8, 1, 3))
print(result3)