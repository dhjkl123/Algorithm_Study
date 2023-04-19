import sys

N = int(sys.stdin.readline())

tmp = 1

for i in range(2,N+1):
    tmp *= i

tmp = reversed(str(tmp))

cnt = 0
for t in tmp:
    if t != '0':
        print(cnt)
        break
    else:
        cnt += 1

