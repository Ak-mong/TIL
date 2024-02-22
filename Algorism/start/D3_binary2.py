import sys; sys.stdin =open('txt/binary2.txt')
t = int(input())
for tc in range(1,t+1):
    n = float(input())
    str = ''
    while n != 1:
        n *= 2
        if n > 1:
            n -= 1
            str += '1'
        elif n < 1:
            str += '0'
        else:
            str += '1'
            break
    if len(str) < 13: print(f"#{tc} {str}")
    else: print(f"#{tc} overflow")
    # print(str)

