import sys

N, K = map(int,sys.stdin.readline().split())

d = [[0] * (K+1) for _ in range(N+1)]

for i in range(1,N+1):
    W, V = map(int,sys.stdin.readline().split())

    for j in range(K+1):
        if j - W < 0:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j-W] + V, d[i-1][j])

print(d[-1][-1])

