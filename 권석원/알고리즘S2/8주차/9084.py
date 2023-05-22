import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int,sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    coin_cnt = len(coins)

    d = [[0] * (M+1) for _ in range(coin_cnt)]

    for i in range(coin_cnt):
        coin = coins[i]
        for j in range(M+1):
            if j == 0:
                d[i][j] = 1
            elif j >= coin:
                d[i][j] = d[i][j-coin] + d[i-1][j]
            else:
                d[i][j] = d[i-1][j]

    print(d[-1][-1])


