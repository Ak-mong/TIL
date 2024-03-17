n = int(input())
member = []
for i in range(1,n+1):
    age, name = map(str,input().split())
    age = int(age)
    member_one = [age,name,i]
    member.append(member_one)
member.sort(key=lambda x: (x[0],x[2]))
# print(member)
for j in member:
    print(*j[:2])