import sys
from collections import deque

N,M,K = map(int,sys.stdin.readline().split())

map_list = [[0] * (N+1) for _ in range(N+1)]

pos_list = []

for _ in range(M):
    r,c,m,s,d = map(int,sys.stdin.readline().split())
    map_list[r][c] = [m,s,d]
    pos_list.append((r,c))

pos_list = deque(pos_list)
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


for _ in range(K):
    
    tmp = []

    while pos_list:
        y,x = pos_list.popleft()
        m, s, d = map_list[y][x]

        nx, ny = x + dx[d], y + dy[d]

        if nx < 0 : nx = N + nx
        if ny < 0 : ny = N + nx
        if nx > N : nx = nx - N
        if ny > N : ny = ny - N

        if map_list[ny][nx] : 
           map_list[ny][nx].append(map_list[y][x])
           tmp.append((ny,nx))

        else:
            map_list[ny][nx] = [m,s,d]
            map_list[y][x] = 0

    for y,x in tmp :
        if len(map_list[y][x]) > 1:
            sum_m = 0
            sum_s = 0
            pre_d = map_list[y][x][0][2]
            flag = False

            for temp in map_list[y][x]:
                m, s, d = temp
                sum_m += m
                sum_s += s

                if pre_d%2 != d%2:
                    flag = True
            
            res_m = sum_m//5
            res_s = sum_s//len(map_list[y][x])

            if flag:
                d_list = [0,2,4,6]
                
            else:
                d_list = [1,3,5,7]
                
            
            

            



            

            



