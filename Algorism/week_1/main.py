import sys;sys.stdin = open('txt/electric_bus')
T = int(input())
for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    M_list = list(map(int, input().split()))
    charg_list = [0] * (N + 1)

    for i in M_list:
        charg_list[i] = 1

    count = 0
    bus_idx = 0

    for i in range(N):
        if bus_idx + K >= N:
            break
        charge = 0

        for j in range(bus_idx + K, bus_idx, -1):
            if 0 < j <= N and charg_list[j]:
                bus_idx = j
                count += 1
                charge = 1
                break

        if charge == 0:
            count = 0
            break
    print(f'#{t} {count}')