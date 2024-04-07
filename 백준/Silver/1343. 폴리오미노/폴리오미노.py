# 1343 폴리오미노 실버5
path = input()
path = path.replace('XXXX','AAAA')
path = path.replace('XX','BB')
if 'X' in path:
    print(-1)
else:
    print(path)