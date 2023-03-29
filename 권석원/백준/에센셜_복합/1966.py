import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int,sys.stdin.readline().split())

    num_list = deque(list(map(int,sys.stdin.readline().split())))

    check_list = [False] * N
    check_list[M] = True
    check_list = deque(check_list)

    cnt = 1

    while num_list:
        max_val = max(num_list)
        
        while max_val != num_list[0]:
            num_list.append(num_list[0])
            num_list.popleft()

            check_list.append(check_list[0])
            check_list.popleft()
        
        num_list.popleft()

        if check_list[0]:
            print(cnt)
        
        check_list.popleft()
        
        cnt += 1
