import sys

T = int(sys.stdin.readline())

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,12):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1] 

for _ in range(T):
    N = int(sys.stdin.readline())
    print(dp[N])



