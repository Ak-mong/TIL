# print(7 & 5)
# print(0b111 & 0b101)
# print(bin(0b111 & 0b101))
#
# print(bin(10))
# print(hex(10))


# if x & 0x01:
#     print('홀수')
# else:
#     print('짝수')

# a = 123
# b = 123.455
# c = 123.355
# d = 123.5
# e = 122.5
#
# print('%d %.2f' % (a,b))
# print('%d %.2f' % (a,c))
# print('%d %.0f' % (a,b))
# print('%d %.0f' % (a,c))
# print()
# print(round(d,0))
# print(round(e,0))
# print(int(d+0.5))
# print(int(e+0.5))
# print()
# print(f'{a:4d} {d:.0f}')
# print(f'{a:4d} {e:.0f}')

# 0000000111100000011000000111100110000110000111100111100111111001100111
# 0 120 12 7 76 24 60 121 124 103
a = '0000000111100000011000000111100110000110000111100111100111111001100111'
# arr = list(map(int,input()))
# n = len(arr)
#
# for i in range(0,n,7):
#     v = 0
#     for j in range(i,i+7):
#         v = v*2 + arr[j]
#     print(v, end=' ')
''''''
for item in range(0,len(a),7):
    # print(a[item:item+7])
    # bin_a = bin(int(''.join(map(str,a[item:item+7]))))
    # print(bin_a)
    bin_a2 = a[item:item+7]
    v = 0
    for j in range(len(bin_a2)):
        v = v * 2 + int(bin_a2[j])
    print(v, end=' ')