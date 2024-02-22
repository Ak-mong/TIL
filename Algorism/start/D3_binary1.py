import sys;sys.stdin = open('txt/binary1.txt')
t = int(input())
dict_hexa = {
    '0':[0,0,0,0],
    '1':[0,0,0,1], # 1
    '2':[0,0,1,0], # 2
    '3':[0,0,1,1], # 3
    '4':[0,1,0,0], # 4
    '5':[0,1,0,1], # 5
    '6':[0,1,1,0], # 6
    '7':[0,1,1,1], # 7
    '8':[1,0,0,0], # 8
    '9':[1,0,0,1], # 9
    'A':[1,0,1,0], # 10(A)
    'B':[1,0,1,1], # 11(B)
    'C':[1,1,0,0], # 12(C)
    'D':[1,1,0,1], # 13(D)
    'E':[1,1,1,0], # 14(E)
    'F':[1,1,1,1],
}
for tc in range(1,t+1):
    n, n16 = map(str,input().split())
    # print(n16)
    new_str = []
    for item in n16:
        new_str += dict_hexa[item]
    # print(new_str)
    print(f"#{tc} {''.join(map(str,new_str))}")