# 순열 : 뽑고 줄세우기
# 조합 : 뽑기
# 중복 순열 > 순열 > 중복조합 > 조합


def comb(level, start):
    if level == r:
        print(path)
        return

    for i in range(start,n):
        path.append(arr[i])
        comb(level+1,i+1)
        path.pop()




# 반복 조합 4C3
arr = [1,2,3,4]
n = len(arr)
r = 3
path = []
comb(0,0)