import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    input_list = []

    for _ in range(2):
        input_list.append(list(map(int,sys.stdin.readline().rstrip().split())))
    
    if N > 1:
        d = [[0] * N for _ in range(2)] #d[0:윗줄, 1:아랫줄][번째]
        d[0][0] = input_list[0][0]
        d[1][0] = input_list[1][0]

        d[0][1] = input_list[0][1] + input_list[1][0]
        d[1][1] = input_list[1][1] + input_list[0][0]
        ans = 0

        for i in range(2,N):
            d[0][i] = max(d[0][i-2] + input_list[0][i],
                        d[1][i-2] + input_list[0][i],
                        d[1][i-1] + input_list[0][i], d[0][i])
            
            d[1][i] = max(d[0][i-2] + input_list[1][i],
                        d[1][i-2] + input_list[1][i],
                        d[0][i-1] + input_list[1][i], d[1][i])
            
        print(max(d[0][N-1],d[1][N-1]))
    else:
        print(max(input_list[0][0], input_list[1][0]))
        
