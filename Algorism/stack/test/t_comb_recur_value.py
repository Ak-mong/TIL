# 조합_재귀_값
def comb(n, r):
    if r == 0:
        return 1
    elif n<r:
        return 0
    else:
        return comb(n-1,r-1) + comb(n-1,r)

print(comb(50,25)) # 시간 매우 오래걸림
