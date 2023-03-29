import sys

N = int(sys.stdin.readline())

input_list = [0] # 시작층

for _ in range(N):
    input_list.append(int(sys.stdin.readline()))

if N == 1:
    print(input_list[1])

else:

    dp = [[0,0] for _ in range(N+1)] # [현재 계단, 연속해서 밟은 개수]
    dp[1][0] = input_list[1] 
    dp[2][0] = input_list[2] 
    dp[2][1] = input_list[1] + input_list[2]

    for i in range(2,N+1):

        dp[i][0] = input_list[i] + max(dp[i-2][0], dp[i-2][1])
        dp[i][1] = input_list[i] + dp[i-1][0]

    print(max(dp[N][1],dp[N][0]))