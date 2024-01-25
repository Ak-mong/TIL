def get_min(lst):
    min =lst[0]
    for i in lst:
        if min > i:
            min = i
    return min
def get_len(lst):
    count = 0
    for i in lst:
        count += 1
    return count
def get_sum(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum
def get_avg(lst):
    sum = 0
    count = 0
    avg = 0
    for i in lst:
        sum +=i
        count += 1
    avg = sum / count
    return avg


lst = [5,7,1,4,6,7,9]
print(f'최소값: {get_min(lst)}')
print(f'갯수: {get_len(lst)}')
print(f'합: {get_sum(lst)}')
print(f'평균: {get_avg(lst)}')

