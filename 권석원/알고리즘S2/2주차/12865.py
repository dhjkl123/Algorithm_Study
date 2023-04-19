import sys

N, K = map(int,sys.stdin.readline().split())

bag_list = []

for _ in range(N):
    bag_list.append(list(map(int,sys.stdin.readline().split())))

d = [[0] * (K+1) for _ in range(N+1)]

for i in range(N):
    w = bag_list[i][0]
    v = bag_list[i][1]
    for j in range(K+1):
        if j >= w:
            d[i+1][j] = max(d[i][j], d[i][j-w] + v)
        else:
            d[i+1][j] = d[i][j]

        
print(d[N][K])

# 가방을 서로 비교하면서 풀려고 했음
# for i in range(N):
#     for j in range(i+1,N):
#         if d[i][j-1][1] + bag_list[j] <= K:
#             d[i][j][0] = max(d[i][j-1][0] + bag_list[j], bag_list[i] + bag_list[j])
#             if d[i][j-2][1] + bag_list[j] <= K:
#                 d[i][j][0] = max(d[i][j][0], d[i][j-2][0] + bag_list[j])
#         else:
#             pass
