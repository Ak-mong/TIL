def itoa(num): # 2진수를 array로
    num_arr = []
    while num:
        num_arr.append(num % 10)
        num //= 10
    num_arr.reverse()
    return num_arr

def atoi(arr): # array를 10진수로
    value = 0
    for item in arr:
        value = value * 2 + item
    return value

bin_num = 10110

print(itoa(bin_num))
print(atoi(itoa(bin_num)))