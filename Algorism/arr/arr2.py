n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr2 = [[0] * n for _ in range(n)]
arr3 = [[0]*n]*n # 얕은 복사라서 하면 안된다.
print('처리안한 arr3',arr3)
arr3[0][0] = 1
print('[0][0] =1 인 arr3',arr3)
arr2[0][0] = 1
print('[0][0] =1 인 arr2',arr2)
