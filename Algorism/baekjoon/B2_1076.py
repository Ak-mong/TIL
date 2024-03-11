import sys;sys.stdin= open('input.txt')
'''
'''
dict = {'black': 1,'brown': 10,'red': 100,'orange': 1000,'yellow': 10000,'green': 100000,
        'blue': 1_000_000,'violet': 10_000_000,'grey': 100_000_000,'white': 1_000_000_000}
dict2 = {'black':'0','brown':'1','red':'2','orange':'3','yellow':'4','green':'5',
        'blue':'6','violet':'7','grey':'8','white':'9'}
sum_v = 0
string = ''
arr = []
for i in range(3):
    arr.append(input())
# print(arr)
string = dict2[arr[0]] + dict2[arr[1]]
# print(string)
sum_v += int(string) * dict[arr[2]]
print(sum_v)
