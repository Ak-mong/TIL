'''
중복 순열, branch = 4, level = 5
'''
path = []
card = ['a','j','q','k']
def count_three():
    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True
    return False
def perm(x):
    global cnt
    if x == 5:
        # print(path)
        if count_three() : cnt += 1
        return
    for i in range(4):
        path.append(card[i])
        perm(x+1)
        path.pop()
cnt = 0
perm(0)
print(cnt)