import sys
from collections import deque

N = int(sys.stdin.readline())

map_list = []

for _ in range(N):
    map_list.append(list(map(int,sys.stdin.readline().split())))


ans = [[0] * N for _ in range(N)]

for k in range(N):
    q = deque([k])
    check = [True] * N
    while q:
        pop = q.popleft()
        
        for i,num in enumerate(map_list[pop]):
            if num:
                ans[k][i] = 1
                if check[i]:
                    q.append(i)
                    check[i] = False
    print(*ans[k])

