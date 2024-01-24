def find_min_max(lst):
    return (min(lst), max(lst))

def find_min_max_2(lst):
    min = max = list[0]
    for num in lst:
        if min >num:
            min = num
        if max < num:
            max = num
    return min,max

result = find_min_max([3,1,7,2,5])
print(result)
result = find_min_max_2([3,1,7,2,5])
print(result)