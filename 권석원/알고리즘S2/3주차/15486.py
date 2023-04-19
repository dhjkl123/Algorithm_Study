import sys

N = int(sys.stdin.readline())

days = [0] * (N+1)
max_money = 0
for i in range(N):
    day, money = map(int,sys.stdin.readline().split())

    if i + day <= N:
        days[i + day] = max(days[i + day], money + days[i], max_money + money)
    
    max_money = max(max_money, days[i])

print(max(max_money,days[N]))


