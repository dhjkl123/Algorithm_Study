import sys
from collections import deque

N = int(sys.stdin.readline())

M = int(sys.stdin.readline())

line = sys.stdin.readline().rstrip()

ans = 0
if 'I' in line:
    i = line.index('I')
else:
    i = 0

def func(idx):
    pre_idx = 'I'
    cnt = 1
    for i in range(idx+1,len(line)):
        if pre_idx != line[i]:
            pre_idx = line[i]
            cnt += 1
        else:
            break
    return cnt


while i < len(line):
    if line[i] == 'I':
        cnt = func(i)

        if cnt>=3:         
            if cnt%2 == 0:
                cnt -= 1
            
            tmp = (cnt-1)//2 - N +1

            if tmp > 0:
                ans += tmp

        i += cnt

    else:
        i += 1


print(ans)
