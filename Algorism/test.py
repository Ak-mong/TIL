import sys;
sys.stdin =open('input.txt')

string = input()
n = len(string)
new_arr = []
for i in range(0,n): # 3 부분으로 나누기
    for j in range(i+1,n-1): # 나머지를 2부분으로 나누기
        strip1 = string[:i+1]
        strip2 = string[i+1:j+1]
        strip3 = string[j+1:]
        new_arr.append(strip1[::-1]+strip2[::-1]+strip3[::-1])
        # print('here',(i,j),strip1,strip2,strip3)
        # print('endd',(i,j),strip1[::-1],strip2[::-1],strip3[::-1])
new_arr.sort()
print(new_arr[0])