import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int,sys.stdin.readline().split())

    q = deque(list(map(int,sys.stdin.readline().split())))

    q_check = deque([False] * N)
    q_check[M] = True
    max_val = max(q)
    cnt = 1
    while q:
        
        val = q.popleft()

        if val == max_val:
            if q_check.popleft():
                print(cnt)
                break

            max_val = max(q)
            cnt += 1
            
        else:
            q.append(val)
            check = q_check.popleft()
            q_check.append(check)
        
        

        



