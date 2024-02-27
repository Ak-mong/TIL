import sys;sys.stdin =open('input.txt')

card = ['a','k','q','j']
path = []
def same_card():
    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True
    return False
def twistedpated(x):
    global cnt
    if x == 5: # 5장 뽑아야된다.
        if same_card(): cnt += 1
        return
    for i in range(4): # 4종류의 카드
        path.append(card[i])
        twistedpated(x+1)
        path.pop()
cnt = 0
twistedpated(0)
print(cnt)