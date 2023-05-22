import sys

N, M = map(int,sys.stdin.readline().split())

map_list = []

for _ in range(N):
    map_list.append(list(map(int,sys.stdin.readline().split())))

dx = [
    [0,1,2,3],[0,0,0,0], # -
    [0,1,0,1],                                  # 네모
    [0,-1,0,1],[0,-1,0,1],[0,0,-1,0],[0,0,1,0], # ㅗ
    [0,0,1,1],[0,-1,-1,-2],[0,1,1,2],[0,0,-1,-1], # ㄹ
    [0,0,0,1],[0,0,1,2],[0,0,-1,-2],[0,1,1,1], # ㄴ
    [0,1,1,1],[0,0,1,2],[0,-1,-1,-1],[-1,0,1,1] # ㄱ
]

dy = [
    [0,0,0,0],[0,1,2,3],
    [0,0,1,1],
    [0,0,-1,0],[0,0,1,0],[0,-1,0,1],[0,-1,0,1],
    [0,1,1,2],[0,0,-1,-1],[0,0,-1,-1],[0,1,1,2],
    [0,-1,-2,-2],[1,0,0,0],[0,1,1,1],[0,0,1,2],
    [0,0,-1,-2],[0,1,1,1],[0,0,-1,-2],[0,0,0,1]
]

ans = 0

for i in range(N):
    for j in range(M):
        for k in range(19):
            tmp = 0
            for n in range(4):
                nx = j + dx[k][n]
                ny = i + dy[k][n]

                if nx < 0 or nx >= M or ny < 0 or ny >= N:
                    tmp = 0
                    break

                tmp += map_list[ny][nx]
            
            ans = max(ans,tmp)

print(ans)
