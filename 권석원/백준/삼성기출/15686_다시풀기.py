import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())

store_list = []
house_list = []

def cal_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for i in range(N):
    tmp =list(map(int,sys.stdin.readline().split()))
    for j in range(len(tmp)):
        if tmp[j] == 1:
            house_list.append((j,i))
        elif tmp[j] == 2:
            store_list.append((j,i))

dist_list = []

answer = 1e10
dists = []

# 각 치킨집으로 부터 치킨 거리를 모두 구해놓기
for store in store_list:
    tmp = []
    for house in house_list:
        tmp.append(cal_dist(store,house))
    dists.append(tmp)

def dfs(depth, selects, k):
    global answer

    if depth == M:
        temp = [1e10] * len(house_list)
        for i in selects:
            for j in range(len(house_list)):
                temp[j] = min(temp[j], dist_list[i][j])
        ans = min(ans,sum(temp))
        return

    for i in range(k, len(store_list)):
        selects.append(i)
        dfs(depth + 1, selects, i + 1)
        selects.pop()
    return

dfs(0, [], 0)


# for store in store_list:
#     tmp = []
#     for house in house_list:
#         tmp.append(cal_dist(store,house))
#     dist_list.append(tmp)

# ans = 1e10

# def dfs(idx, select, cnt): #idx 매장 위치, cnt 매장 개수
#     global ans

    # if cnt == M:
    #     temp = [1e10] * len(house_list)
    #     for i in select:
    #         for j in range(len(house_list)):
    #             temp[j] = min(temp[j], dist_list[i][j])
    #     ans = min(ans,sum(temp))
    #     return
    
#     for i in range(idx, len(store_list)):
#         select.append(i)
#         dfs(idx + 1 ,select, cnt+1)
#         select.pop()
#     return

# dfs(0,[],0)

print(answer)

