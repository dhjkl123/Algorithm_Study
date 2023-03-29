import sys

n,m = map(int,sys.stdin.readline().split())

input_list = []
dp_list = [[0]*(n+1)]
pre_lisn_sum = 0

for i in range(n):
    tmp_list = list(map(int,sys.stdin.readline().split()))
    dp_tmp = [0]

    if i == 0:
        tmp_sum = 0
        for tmp in tmp_list:
            tmp_sum += tmp
            dp_tmp.append(tmp_sum)
    else:
        tmp_sum = 0
        for j in range(n):
            tmp_sum += tmp_list[j]
            dp_tmp.append(dp_list[i][j+1] + tmp_sum)

    dp_list.append(dp_tmp)
    input_list.append(tmp_list)



for _ in range(m):
    x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
    ans = dp_list[x2][y2] - (dp_list[x1-1][y2] + dp_list[x2][y1-1]) + dp_list[x1-1][y1-1]
    
    print(ans)