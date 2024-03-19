import sys;
# 2941 크로아티아 알파벳 실버5
croal_alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
str_v = sys.stdin.readline().rstrip()
cnt = 0
for i in croal_alphabet:
    if i in str_v:
        cnt += str_v.count(i)
        str_v = str_v.replace(i,'8')
str_v = str_v.replace('8','')
cnt += len(str_v)

print(cnt)