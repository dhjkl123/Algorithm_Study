import sys
import math
A, B, V = map(int,sys.stdin.readline().split())

if (V-A) > (A-B):
    ans =  math.ceil((V-A)/(A-B)) + 1 # 정상을 넘어서거나 도착한다면 밤으로 갈 필요 없음 즉 정상에 도달하기 직전에 몇일이 필요한지
else:
    if V == A: # 하루면 도착
        ans = 1
    else: # 맨 처음 if와 같은 이유
        ans = 2


print(ans)