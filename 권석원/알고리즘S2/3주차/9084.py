import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int,sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    m_list = [[0] * (M+1) for _ in range(N)]

    for i in range(N):
        m_list[i][0] = 1
        coin = coins[i]
        for j in range(1,M+1):       
            if j - coin >= 0 : m_list[i][j] += m_list[i][j - coin]
            if i > 0 : m_list[i][j] += m_list[i-1][j]

    print(m_list[N-1][M])