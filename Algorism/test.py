<<<<<<< HEAD
# import sys;sys.stdin =open('input.txt')
=======
import sys;sys.stdin =open('input.txt')

def get_result():
    cnt = 0
    for i in range(n): # arr 한바퀴 도는것
        i_b = arr[i][1]
        for j in range(i): # i 와 그 전 인덱스들을 비교하겠다
            j_b = arr[j][1]
            if i_b < j_b: # A 전봇대에서는 위에 있는 전선이 B에서는 더 작을 때
                cnt += 1
    return cnt

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [tuple(map(int,input().split())) for _ in range(n)]
    # print(arr)
    # arr.sort(key=lambda x:x[0])
    arr.sort(key=lambda x:x[0])
    # print(arr)
    result = get_result()
    print(f'#{tc} {result}')
>>>>>>> 5a69728f25d66cf46b1f2210b4a07832459f1a63
