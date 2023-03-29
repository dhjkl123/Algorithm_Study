import sys

N = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))

d = [0] * N
d[0] = num_list[0]

for i in range(1,N):
    d[i] = max(num_list[i],num_list[i] + d[i-1])


print(max(d))

