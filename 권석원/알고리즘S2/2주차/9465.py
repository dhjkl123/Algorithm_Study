import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    map_list = []

    for _ in range(2):
        tmp = list(map(int,sys.stdin.readline().split()))
        map_list.append(tmp)
    
    d = [[0] * N for _ in range(2)]
    d[0][0] = map_list[0][0]
    d[1][0] = map_list[1][0]

    if N > 1:
        d[0][1] = d[1][0] + map_list[0][1]
        d[1][1] = d[0][0] + map_list[1][1]

        for i in range(2,N):
            d[0][i] = max(d[1][i-1] + map_list[0][i], d[1][i-2] + map_list[0][i], d[0][i-2] + map_list[0][i])
            d[1][i] = max(d[0][i-1] + map_list[1][i], d[1][i-2] + map_list[1][i], d[0][i-2] + map_list[1][i])
    
    print(max(d[0][N-1],d[1][N-1]))
