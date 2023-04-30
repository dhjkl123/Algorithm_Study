import sys

N = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())

d = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == 0 :
            d[i][j] = 1
        else:
            if i + j < N and num[j] == num[j+i]:
                if i == 1:
                    d[i][j] = d[i-1][j]
                else:
                    d[i][j] = d[i-2][j+1]


for _ in range(M):
    S, E = map(int,sys.stdin.readline().split())
    print(d[E-S][S-1])
