import copy

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


map_list = [[0] * 4 for _ in range(4)]


for k in range(19):
    conti_flag = False
    for i in range(4):
        for j in range(4):
            if not conti_flag:
                flag = True
                tmp_list = copy.deepcopy(map_list)
                for n in range(4):
                    nx = j + dx[k][n]
                    ny = i + dy[k][n]

                    if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                        flag = False
                        break

                    tmp_list[ny][nx] = 1
                if flag:
                    print(k)
                    conti_flag = True
                    for tmp in tmp_list:
                        print(tmp)
                    print()
