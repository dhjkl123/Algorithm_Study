import sys

N, K = map(int,sys.stdin.readline().split())
bag_list = []

for _ in range(N):
    bag_list.append(tuple(map(int,sys.stdin.readline().split())))

ans = 0

def func(idx,total_w,total_v):
    global ans

    if idx == N :
        if total_w <= K:
            ans = max(ans,total_v)
        return

    if total_w + bag_list[idx][0] > K:
        ans = max(ans,total_v)
        return

    
    func(idx+1,total_w+bag_list[idx][0],total_v+bag_list[idx][1])
    func(idx+1,total_w,total_v)

func(0,0,0)

print(ans)