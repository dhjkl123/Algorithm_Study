import sys

N = int(sys.stdin.readline())

input_list = []

for _ in range(N):
    input_list.append(list(map(int,sys.stdin.readline().split())))

d = [0] * (N + 1)
max_val = 0
ans = 0

for i in range(0,N):
    day = input_list[i][0]
    cost = input_list[i][1]
    max_val = max(max_val,d[i])

    if i + day <= N: # 오늘 일을 맡아도 퇴사를 하지 않을 때
        d[i + day] = max(d[i + day],d[i] + cost, max_val + cost) #오늘 일 안하고 day 후, 오늘 일하고 day 후, 마지막에 가장 많일 번 후 오늘 일 할때
        ans = max(d[i + day], ans)


print(ans)
