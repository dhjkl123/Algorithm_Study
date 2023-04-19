import sys

N = int(sys.stdin.readline())

num_list = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())

my_list = [[0] * N for _ in range(N)]

my_list[N-1][N-1] = 1

for i in range(N-1,-1,-1):
    for j in range(N-1,i-1,-1):
        if i >= N-1 : 
            continue

        if i == j : 
            my_list[i][j] = 1
        elif i+1 == j : 
            my_list[i][j] = 1 if num_list[i] == num_list[j] else 0
        else: 
            my_list[i][j] = 1 if my_list[i+1][j-1] and num_list[i] == num_list[j] else 0

    
for _ in range(M):
    S, E = map(int,sys.stdin.readline().split())

    print(my_list[S-1][E-1])


