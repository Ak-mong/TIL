import sys;sys.stdin= open('D3_quick_sort.txt')


def partition(arr,left,right): # 피봇 찾기
    pivot = arr[left] # 피봇을 하나 정해두기
    i,j = left, right # left right를 직접 쓸 수 없기 때문
    while i <= j: # 교차하거나 지나칠 때 까지
        while i <= j and arr[i] <= pivot: i += 1
        while i <= j and arr[j] >= pivot: j -= 1
        if i < j: # 인덱스 i 가 j 보다 앞에 있을 때
            arr[i],arr[j] = arr[j],arr[i] # 교환한다
    # j 자리에 ㅍ피봇을 넣는다.
    arr[left], arr[j] = arr[j],  arr[left]
    return j # 새 피봇이 될 값이 j 기 때문

def quick_sort(arr,left,right): # 퀵 소트 진행
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr,left,pivot-1) # 피봇보다 작은 애들 정렬
        quick_sort(arr,pivot+1,right) # 피봇보다 큰 애들 정렬


t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = list(map(int,input().split()))
    quick_sort(arr,0,len(arr)-1)
    print(f'#{tc} {arr[n//2]}')
















# def quick(arr,l,r):
#     pbot = arr[l]
#     i,j = l,r
#     while  i <= j:
#         while i <= j and arr[i]<= pbot: i += 1
#         while i <= j and arr[j] >= pbot: j -= 1
#         if i < j: arr[i],arr[j] = arr[j],arr[i]
#     # 다 끝나고 나서
#     arr[l] , arr[j] = arr[j], arr[l]
#     return j
#
# def quick_sort(arr,l,r):
#     if l < r:
#         pivot = quick(arr,l,r)
#         quick_sort(arr,l,pivot-1)
#         quick_sort(arr,pivot+1,r)
