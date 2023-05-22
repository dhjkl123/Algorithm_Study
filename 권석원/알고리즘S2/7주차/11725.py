import sys
from collections import deque

N = int(sys.stdin.readline())

map_list = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    map_list[a].append(b)
    map_list[b].append(a)


ans_list = [0] * (N+1) 
q = deque([1])
check = [False] * (N+1)
check[1] = True

while q:
    parent = q.popleft()

    for i in map_list[parent]:
        if not check[i]:
            ans_list[i] = parent
            check[i] = True
            q.append(i)

for i in range(2,len(ans_list)):
    print(ans_list[i])