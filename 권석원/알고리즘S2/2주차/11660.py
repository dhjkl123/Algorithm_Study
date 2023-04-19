import sys

N, M = map(int, sys.stdin.readline().split())

map_list = []
d_list = [[0] * N for _ in range(N)]

for i in range(N):
    map_list.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):

        sum = map_list[i][j]

        if j > 0:
            sum += d_list[i][j-1]
        
        if i > 0:
            sum += d_list[i-1][j]
        
        if j > 0 and i > 0:
            sum -= d_list[i-1][j-1]

        d_list[i][j] = sum

for _ in range(M):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1 
    if x1 == x2 and y1 == y2:
        print(map_list[x1][y1])
    else:
        if x1 == 0 and y1 == 0:
            ans = d_list[x2][y2]
        else:
            ans = d_list[x2][y2]

            if x1 - 1 >= 0:
                ans -= d_list[x1-1][y2]

            if y1 - 1 >= 0:
                ans -= d_list[x2][y1-1] 

            if  x1 - 1 >= 0 and y1 - 1 >= 0:
                ans += d_list[x1-1][y1-1]

        print(ans)