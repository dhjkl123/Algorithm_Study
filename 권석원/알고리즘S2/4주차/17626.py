import sys

N = int(sys.stdin.readline())

d = [1e9] * (N+1)
d[1] = 1

num = [1]


for i in range(2,N+1):
    tmp = int(pow(i,(1/2)))
    if pow(i,(1/2)) - tmp > 0:
        for j in num:
            d[i] = min(d[i], 1 + d[i - j])
    else:
        d[i] = 1
        num.append(i)

    

print(d[N])