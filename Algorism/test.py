import sys;
sys.stdin =open('input.txt')
import time
starttime = time.time()

t = int(input())
for tc in range(1,t+1):
    n = float(input())
    str = ''
    while n != 0:
        n *= 2
        if n >= 1:
            n -= 1
            str += '1'
        elif n < 1:
            str += '0'
        if len(str) > 12:
            str = 'overflow'
            break
    print(str)

