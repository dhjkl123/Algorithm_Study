import sys
from collections import deque
M, N = map(int,sys.stdin.readline().split())

box_list = []
check_list = [[0] * M for _ in range(N)]
q = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(N):
    tmp_list = list(map(int,sys.stdin.readline().split()))
    for j in range(M):
        if tmp_list[j] == 1:
            q.append([j,i])
            tmp_list[j] = 0
            check_list[i][j] = 1 # 이미 방문
        
        elif tmp_list[j] == -1:
            check_list[i][j] = 2 # 토마토 없음

            
    box_list.append(tmp_list)

ans = 0

while q:
    x,y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= M: continue
        if ny < 0 or ny >= N: continue
        if box_list[ny][nx] == -1: continue
        if check_list[ny][nx]: continue

        if box_list[ny][nx] == 0:
            box_list[ny][nx] = box_list[y][x] + 1
        else:
            box_list[ny][nx] = min(box_list[ny][nx], box_list[y][x] + 1)
            if box_list[ny][nx] != box_list[y][x] + 1: continue
        
        check_list[ny][nx] = 1
        q.append([nx,ny])



for i in range(N):
    if 0 in check_list[i]:
        ans = -1
        break

    tmp = max(box_list[i])
    ans = max(tmp,ans)


print(ans)


