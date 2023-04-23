import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())

map_list = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int,sys.stdin.readline().split())
    map_list[A].append(B)
    map_list[B].append(A)

min_num = 1e9
ans = 1e9

for i in range(1,N+1):
    q = deque([i])
    visited = [i]
    cnt = [0] * (N+1)

    while q:
        idx = q.popleft()

        for m in map_list[idx]:
            
            if cnt[m] == 0 and m != i:
                cnt[m] = cnt[idx] +1
            else:
                cnt[m] = min(cnt[idx] +1, cnt[m])

            if m not in visited:
                visited.append(m)
                q.append(m)

    if min_num >= sum(cnt):
        if min_num == sum(cnt):
            ans = min(i,ans)
        else:
            ans = i
            min_num = sum(cnt)

print(ans)

