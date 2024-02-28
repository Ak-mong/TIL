# def powerset(n,k):
#     if k == n:
#         print(bit)
#         return
#     bit[k] =1
#     powerset(n,k+1)
#     bit[k] = 0
#     powerset(n, k + 1)
# arr = [1,2,3]
# n = len(arr)
# bit = [0] * n
# powerset(n,0)

friends = ['a','b','c','d','e']

def find(x):
    global cnt
    if x == len(friends):
        if sum(fd) >=2:
            cnt += 1
            # print(fd)
        return
    fd[x] = 1
    find(x + 1)
    fd[x] = 0
    find(x + 1)

fd = [0] * len(friends)
n = len(friends)
cnt = 0
find(0)
print(cnt)
