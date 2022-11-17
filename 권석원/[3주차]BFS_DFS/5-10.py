from collections import deque
import sys

N,M = map(int,sys.stdin.readline().split())

map_list = []
check_list = []

for i in range(N):
    tmp = sys.stdin.readline().rstrip()
    tmp_list = []
    for c in tmp:
        tmp_list.append(int(c))
    
    map_list.append(tmp_list)
    check_list.append([0]*M)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

que = deque([])
cnt = 0

for i in range(N):
    for j in range(M):
        if map_list[i][j] == 0 and check_list[i][j] == 0:
            
            cnt += 1
            que.append([j,i])
            
            while que:
                k = que.popleft()
                x,y = k[0],k[1]
                
                check_list[y][x] = 1
                
                for n in range(4):
                    nx = x + dx[n]
                    ny = y + dy[n]
                    
                    if nx < 0 or nx >= M : continue
                    if ny < 0 or ny >= N : continue
                    
                    if map_list[ny][nx] == 1 : continue
                    if check_list[ny][nx] == 1 : continue
                    
                    que.append([nx,ny])
                    
                    
print(cnt)    
    