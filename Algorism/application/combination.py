friends = ['a','b','c','d','e']
m = 5 # 친구의 수
n = 3
path = []
# 5C2
def getFriend(lev, start):
    if lev ==n:
        print(path)
        return

    for i in range(start,5):
        path.append(friends[i])
        getFriend(lev + 1, i+1)
        path.pop()

getFriend(0,0)

arr = ['a','b','c','d','e']
# n = 3
len_arr = len(arr)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
print(factorial(len_arr) // (factorial(n) * factorial(len_arr-n))   )