'''
branch = 1~6
level  = 3
중복순열
'''
path = []
def perm(x,sum):
    global cnt
    if sum > 10: # 가지치기
        return
    if x ==3:
        cnt += 1
        # print(f'{path} : {sum}')
        return
    for i in range(1,7):
        path.append(i)
        perm(x+1, sum + i )
        path.pop()

cnt = 0
perm(0,0)
print(cnt)