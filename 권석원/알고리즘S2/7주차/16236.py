import sys
from collections import deque

N = int(sys.stdin.readline())

map_list = []           # 공간 

shark_pos = [-1,-1]     # 상어의 현재위치 
shark_level = 2         # 상어의 크기 
shark_cnt = 0           # 상어가 먹은 물고기 수 / 크기가 커지면 다시 0으로기

fish_list = []
ans = 0

for i in range(N):
    tmp =list(map(int,sys.stdin.readline().split()))
    for j in range(len(tmp)):
        if tmp[j] == 9 : # 상어 좌표를 얻고 자리는 0으로 대체
            tmp[j] = 0
            shark_pos = [j,i]
        elif tmp[j] > 0 : # 먹이 좌표 얻기 
            fish_list.append([j,i])

    map_list.append(tmp)

fish_list.sort(key= lambda x : (x[1],x[0]))

def findFish(level):
    pos_list = []
    for fish in fish_list:
        x,y = fish
        if map_list[y][x] < level:
            pos_list.append([x,y])
    
    return pos_list # 물고기 위치 

def getFish(pos_list):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    return_list = []

    for pos in pos_list:
        q = deque([shark_pos])
        map_dist = [[0] * N for _ in range(N)]

        while q:
            x,y = q.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                if shark_pos[0] == nx and shark_pos[1] == ny: continue
                if map_dist[ny][nx] != 0: continue
                if map_list[ny][nx] > shark_level: continue # 아기 상어보다 큰 물고기는 지나칠 수 없다 

                if nx == pos[0] and ny == pos[1]:
                    return_list.append([map_dist[y][x] + 1,pos])
                    q.clear()
                    break
                else:
                    map_dist[ny][nx] = map_dist[y][x] + 1
                    q.append([nx,ny])
    
    return return_list # 아기 상어보다 크기가 작은 물고기 중 먹을 수 있는 물고기 

while fish_list: # 더 이상 먹을 물고기가 없다면 엄마 상어 호출 
    pos_list = findFish(shark_level) # 아기상어보다 작은 물고기 찾기    
    pos_list = getFish(pos_list) # 작은 물고기 찾기 중 먹을 수 있는 물고기 찾기 

    if len(pos_list) == 0 : # 더 이상 먹을 물고기가 없다면 엄마 상어 호출 
        break
    
    pos_list.sort(key=lambda x : (x[0],x[1][1],x[1][0]))

    shark_pos = pos_list[0][1]
    shark_cnt += 1
    ans += pos_list[0][0]

    # 물고기를 먹었으면 해당 위치 0으로 
    x,y = pos_list[0][1]
    map_list[y][x] = 0
    for i in range(len(fish_list)):
        if fish_list[i][0] == x and fish_list[i][1] == y:
            del fish_list[i]
            break

    if shark_level == shark_cnt: # 아기 상어크기 만큼 물고기를 먹으면 크기 증가
        shark_level += 1
        shark_cnt = 0

print(ans)