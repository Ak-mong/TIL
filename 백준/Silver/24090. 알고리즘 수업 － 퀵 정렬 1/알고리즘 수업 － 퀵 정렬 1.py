import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)
# 알고리즘 수업- 퀵정렬 1 24090 실버5
n,k = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
def quick_sort(p,r): # A[p..r]을 오름차순 정렬한다.
    if p >=r: return
    q = partition(p, r)  # 분할
    quick_sort(p, q - 1)  # 왼쪽 부분 배열 정렬
    quick_sort(q + 1, r)  # 오른쪽 부분 배열 정렬

def partition(start, end):
    global cnt
    x = arr[end]    # 기준원소
    i = start-1   # i는 x보다 작거나 작은 원소들의 끝지점
    for j in range(start,end):
        if arr[j] <= x:
            cnt += 1
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
            if cnt == k:
                print(arr[i],arr[j])
                exit()
    if i + 1 != end:
        arr[i + 1],arr[end] = arr[end],arr[i+1] # i + 1과 r이 서로 다르면 A[i + 1]과 A[r]을 교환
        cnt += 1
        if cnt == k:
            print(arr[i+1], arr[end])
            exit()
    return i + 1

quick_sort(0,n-1)
if k > cnt: print(-1)