import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

# 2776 암기왕 실버4

def find_value(x):
    s = 0
    e = n-1
    while s <= e:
        mid = (s + e) // 2
        if x == note1[mid]:
            return 1
        elif x < note1[mid]:
            e = mid -1
        elif x > note1[mid]:
            s = mid + 1
    return 0
t = int(input())
for _ in range(t):
    n = int(input())
    note1 = list(map(int,input().split()))
    m = int(input())
    note2 = list(map(int,input().split()))
    note1.sort()
    for i in note2:
        print(find_value(i))