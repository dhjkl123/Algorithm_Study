import sys

N = int(sys.stdin.readline())

rgb_list = []

for _ in range(N):
    rgb_list.append(list(map(int,sys.stdin.readline().split())))

d = [[0,0,0] for _ in range(N)]
d[0] = rgb_list[0]

for i in range(1,N):
    d[i][0] = min(rgb_list[i][0] + d[i-1][1], rgb_list[i][0] + d[i-1][2])
    d[i][1] = min(rgb_list[i][1] + d[i-1][0], rgb_list[i][1] + d[i-1][2])
    d[i][2] = min(rgb_list[i][2] + d[i-1][1], rgb_list[i][2] + d[i-1][0])

print(min(d[N-1]))
