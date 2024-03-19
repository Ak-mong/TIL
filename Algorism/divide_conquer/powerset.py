def powerset(level):
    if level == n:
        # print(bit)
        for i in range(n):
            if bit[i]:
                print(arr[i], end=' ')
        print()
        return

    bit[level] = 1
    powerset(level+1)
    bit[level] = 0
    powerset(level+1)

arr = [1,2,3]
n = len(arr)
bit = [0] * n
powerset(0)