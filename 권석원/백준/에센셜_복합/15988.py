import sys

T = int(sys.stdin.readline())
n = 1000001
d = [0] * n

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4,n):
    d[i] = (d[i-1] + d[i-2] + d[i-3]) % 1000000009

for _ in range(T):
    n = int(sys.stdin.readline())
    print(d[n])
