# 9996 한국이 그리울 땐 서버에 접속하지 실버 3
n = int(input())
find_str1, find_str2 = input().split('*')

arr = []
for _ in range(n):
    a = input()
    arr.append(a)

for i in range(n):
    if find_str1 == arr[i][:len(find_str1)]:
        arr[i] = arr[i].replace(find_str1,'',1)
        if find_str2 != arr[i][-len(find_str2):]:
            print('NE')
        else:
            print('DA')
    else:
        print('NE')