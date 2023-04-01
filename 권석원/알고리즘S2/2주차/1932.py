import sys

N = int(sys.stdin.readline())

tower_list = []

for _ in range(N):
    tower_list.append(list(map(int,sys.stdin.readline().split())))

d = [[0] * N for _ in range(N)]

d[0][0] = tower_list[0][0]

for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            d[i][j] = tower_list[i][j] + d[i-1][j]
        elif j == i:
            d[i][j] = tower_list[i][j] + d[i-1][j-1]
        else:
            d[i][j] = max(tower_list[i][j] + d[i-1][j], tower_list[i][j] + d[i-1][j-1])

print(max(d[N-1]))