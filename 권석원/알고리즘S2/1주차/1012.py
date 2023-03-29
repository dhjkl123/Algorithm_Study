import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):

    M, N, K = map(int,sys.stdin.readline().split())

    pos = []
    map_list = [[0] * M for _ in range(N)]

    for _ in range(K):
        x,y = map(int,sys.stdin.readline().split())
        map_list[y][x] = 1
        pos.append([x,y])
    
    q = deque(pos)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    ans = 0

    while q:
        x,y = q.popleft()

        if map_list[y][x]:
            map_list[y][x] = 0
            ans += 1
            q2 = deque([[x,y]])
            while q2:
                x2,y2 = q2.popleft()
                for i in range(4):
                    nx = x2 + dx[i]
                    ny = y2 + dy[i]

                    if 0 > nx or nx >= M : continue
                    if 0 > ny or ny >= N : continue
                    if map_list[ny][nx] == 0 : continue

                    map_list[ny][nx] = 0
                    q2.append([nx,ny])
    
    print(ans)


    


               