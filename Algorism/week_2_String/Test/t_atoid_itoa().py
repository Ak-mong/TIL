def atoi(arr): # 배열 -> 정수
    v = 0
    for i in range(n):
        v = v * 10 + arr[i]
    return v

def atoi2(str): # 문자열=> 정수
    v = 0
    for i in range(n2):
        v = v * 10 + ord(str[i]) - ord('0')
    return v

def itoa(num): #정수 -> 배열
    result = []
    while num:
        result.append(num % 10)
        num //= 10
    result.reverse()
    return result

def itoa2(num): #정수 -> 문자열
    result = []
    while num:
        result.append(chr((num % 10) + ord('0')))
        num //= 10
    result.reverse()
    return ''.join(result)
num = 123
resulted = itoa(num)
print(resulted,type(resulted))

num = 123
resulted = itoa2(num)
print(resulted,type(resulted))

arr = [1, 2, 3]
n = len(arr)
print(atoi(arr),type(atoi(arr)))

str1 = '123'
n2 = len(str1)
print(atoi2(str1),type(atoi2(str1)))
# 정수로 된 배열을 문자열로 변환
# arr2 = [1,2,3]
# str2 = ''.join(arr2)
# print(str1)