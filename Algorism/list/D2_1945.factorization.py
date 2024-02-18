import sys;sys.stdin = open('txt/factorization.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    fact = 0
    flag = 1 # 나눌 수 있는 수
    fact_list = []
    a_cnt = 0
    b_cnt = 0
    c_cnt = 0
    d_cnt = 0
    e_cnt = 0
    while flag:
        # 소인수가 N가 같다면 나가버린다.
        if N%2 ==0:
            N //= 2
            a_cnt +=1
        elif N%3 ==0:
            N //= 3
            b_cnt +=1
        elif N%5 ==0:
            N //= 5
            c_cnt +=1
        elif N%7 ==0:
            N //= 7
            d_cnt +=1
        elif N%11 ==0:
            N //= 11
            e_cnt +=1
        else:
            break
    print(f'#{tc}',a_cnt,b_cnt,c_cnt,d_cnt,e_cnt)