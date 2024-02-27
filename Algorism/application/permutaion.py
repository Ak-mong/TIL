# def kfc(x):
#     if x ==6:
#         return
#     print(x, end=' ')
#     kfc(x+1)
#     print(x, end=' ')
# def krc(x):
#     print(x)
#     x += 1
#     bts(x +5)
#     print(x)
# def bts(x):
#     print(x)
# x = 3
# krc(x+5)
# print(x)
# kfc(0)
# print('끝')
# def kfc2(x):
#     if x == 3:
#         print(x, end=' ')
#         return
#     print()
#     print(x)
#     kfc2(x+1)
#     kfc2(x+1)
# kfc2(0)
# def run(level):
#     if level ==3:
#         return
#     for i in range(2):
#         run(level+1)
#
# run(0)
path = []
# def type1(x):
#     if x ==3:
#         print(path)
#         return
#     for i in range(1,7):
#         path.append(i)
#         type1(x + 1)
#         path.pop()
# type1(0)

# used = [False,False,False]
# def type2(x):
#     if x == 2:
#         print(path)
#         return
#     for i in range(1,7):
#         if used[i] == True:continue
#         used[i] = True
#         path.append(i)
#         type2(x+1)
#         path.pop()
#         used[i] = False
# # type2(0)
# n, type = map(int,input().split())
# if type == 1:
#     type1(0)
# if type == 2:
#     type1(0)
#
# def funy(y):
#     if y == 4:
#         print(path)
#         return
#     # for i in range(1,7):
#     path.append(1)
#     funy(y+1)
#     path.pop()
#     path.append(2)
#     funy(y + 1)
#     path.pop()
#     path.append(3)
#     funy(y + 1)
#     path.pop()
#     path.append(4)
#     funy(y + 1)
#     path.pop()
#     path.append(5)
#     funy(y + 1)
#     path.pop()
#     path.append(6)
#     funy(y + 1)
#     path.pop()
# funy(1)
# for i in range(3):
#     for j in range(3):
#         print([i,j])
