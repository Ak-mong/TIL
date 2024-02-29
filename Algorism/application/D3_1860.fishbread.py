import sys;sys.stdin=open('txt/fish_bread.txt')
'''
m초당 k개 붕어빵
n명의 사람
n명의 사람이 몇 초 때 마다 오는지
2 2 2
3 4
'''
def start():
    sold_bread = 0
    for person in customers:
        # 공식, 특정 시간에 만들 수 있는 빵의 개수
        made_bread = (person //m) * k

        # 빵을 한개 팔았다
        sold_bread += 1
        # 재고계산
        remain = made_bread - sold_bread
        if remain < 0:
            return 'Impossible'
        return 'Possible'
t = int(input())
for tc in range(1,t+1):
    n,m,k = map(int,input().split()) # n 사람 수 m초당 k개 만든다
    customers = list(map(int,input().split()))
    # arr.sort()
    # print(arr)
    # for i in range(len(customers)):
        # if customers[i]/m * k - (i+1) < 0:
        #     print('imposible')
        # else:
            # print('posible')
    print(start())