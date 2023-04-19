import sys

N, M = map(int,sys.stdin.readline().split())

sqr_list = [['0'] * (M+1)]
d_list = [[0] * (M+1) for _ in range(N+1)]

for _ in range(N):
    line = list('0' + sys.stdin.readline().rstrip())
    sqr_list.append(line)

ans = 0

for i in range(1,N+1):
    for j in range(1,M+1):
        if int(sqr_list[i][j]):
            d_list[i][j] = min(d_list[i-1][j-1], d_list[i-1][j],d_list[i][j-1]) + int(sqr_list[i][j])
        ans = max(ans,d_list[i][j])

print(ans*ans)


