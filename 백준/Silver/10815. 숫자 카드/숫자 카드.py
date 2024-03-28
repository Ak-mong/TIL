'''
상근이 숫자 n개
정수 m개 주어짐
주어진 숫자카드를 상근이가 가지고 있는가?

같은수는 적혀있지 않음, 음수 숫자카드도 존재함

'''
n = int(input())
n_arr = list(map(int,input().split()))
m = int(input())
m_arr = list(map(int,input().split()))
dict_arr = {}
for i in m_arr:
    dict_arr[i] = 0
# print(dict_arr)
for j in n_arr:
    if dict_arr.get(j) ==0 :
        dict_arr[j] += 1
# print(dict_arr)
print(*dict_arr.values())