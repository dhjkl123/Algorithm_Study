import sys

N, K = map(int,sys.stdin.readline().split())

my_list = []

for _ in range(N):
    my_list.append(int(sys.stdin.readline()))

my_list.sort(reverse=True)

ans = 0
tmp = 0

for coin in my_list:

    while K >= tmp + coin:
        tmp += coin
        ans += 1

print(ans)