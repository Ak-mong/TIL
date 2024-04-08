# 10773 제로 실버4 
k = int(input())
stack = []
for i in range(k):
    inputs = int(input())
    if inputs == 0:
        stack.pop()
    else:
        stack.append(inputs)
print(sum(stack))

