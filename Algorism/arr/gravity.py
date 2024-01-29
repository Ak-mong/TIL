'''
9
7 4 2 0 0 6 0 7 0
'''
N = int(input()) # 상자가 쌓여있는 가로 길이
arr = list(map(int,input().split()))
"""
오른쪽으로 자기보다 낮은 애들의 갯수 = 떨어질 수 있는 길이
7 은 7칸을 떨어질수 있겠네 4 2 0 0 6 0 0
4 은 5칸
2는 4칸
0은 0, 0은 0
6은 2개
0은 0개
7은 1개
0은 0개
여기서 최대값을 찾아라 => 7
리스트를 하나 생성하고, max(lst) 로 구하는 흔한 방법 (X) 경고!!

권장방법 : max_v 를 0으로 초기화 하고
0 ~ n-1 (모든 상자에 대해) 
for i:0-> N-1: # 낙차구하는 위치
    cnt <- 0
    for j: i+1 ~ n-1 # i와 비교할 수치
        if arr[i] > arr[j]
            cnt +=1
        if max_v < cnt
        max_v = cnt
"""
max_v = 0 # 가장 큰 낙차
# for i : 0 -> N-2, i 낙차를 구할 위치
for i in range(N-1):
    cnt = 0 # 오른쪽에 있는 더 낮은 높이의 개수
    #for j : i+1 -> N-1
    for j in range(i+1, N):
        if arr[i]>arr[j]:
            cnt +=1
    if max_v < cnt: #최대 낙차보다 크면
        max_v = cnt
print(max_v)

# 연습
max_v = 0 #가장 큰 낙차
for i in range(N-1): #for i : 0 -> N -2 낙차를 구할 위치
    cnt = 0 #오른쪽에 있는 더 낮은 높이의 개수
    for j in range(i+1,N): #for j : i+1-> N-1
        if arr[i] > arr[j]:
            cnt += 1
    if max_v < cnt: #최대 낙차보다 크면
        max_v = cnt
print(max_v)
