# D2_11871.stack1_3
import sys;sys.stdin = open('txt/stack1_3.txt')

t = int(input())
for tc in range(1,t+1):
    n = list(map(str,input()))
    """
    for 문으로 i == a 가 같을 때로 돌린다면?
    연속된 자리가 아니라도 지워진다
    if i == i+1 :
        pop(i) 
        pop(i+1)
    # ABCCB  
    """
    # for i in range(len(n)-1):
    x = 0
    while True:
        try:
            if n[x] == n[x+1]:
                n.pop(x)
                n.pop(x)
                # 이게 처리되면 n의 길이는 달라져있음
                # x가 2,3 일때 지워짐
                # ABB 3개
                # 다음 루프 : 처음으로 돌아가고 나서 x가 1,2 일때 지워짐
                # A 1개
                x = 0
            x += 1
        except IndexError:
            break
    # print(n)
    print(f'#{tc} {len(n)}')
    # print(n[0])