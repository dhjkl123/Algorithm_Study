import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int,sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    d = [[0]*(M+1) for _ in range(N)]

    for i in range(N):
        d[i][0] = 1
        coin = coins[i]
        for j in range(1,M+1):
           if j - coin < 0 :  d[i][j] = d[i-1][j]
           else: d[i][j] = d[i][j-coin] + d[i-1][j]
    
    print(d[-1][-1])
