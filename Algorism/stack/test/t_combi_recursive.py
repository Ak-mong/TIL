# 조합_재귀
def comb(n, r):
    if r == 0:
        return 1
    elif n<r:
        return 0
    else:
        return comb(n-1,r-1) + comb(n-1,r)
print(comb(4,3))
