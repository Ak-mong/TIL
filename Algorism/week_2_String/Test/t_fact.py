# 4!
# 4 3 2 1
n = 4
i = 1
for x in range(1,n+1):
    i *= x
def fact(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
def fact2(n):
    # basis part (멈추는 부분)
    if n ==1:
        return 1
    # inductive part (유도 파트)
    else:
        return n * fact2(n-1)
print(fact(4))
print(fact2(4))

lstork