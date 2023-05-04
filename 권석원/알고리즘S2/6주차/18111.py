import sys

N, M, B = map(int,sys.stdin.readline().split())

map_list = []
ans = 1e9
idx = 0

for _ in range(N):
    map_list.append(list(map(int,sys.stdin.readline().split())))


for target in range(257): # 목표 지반
    max_target, min_target = 0, 0

    for i in range(N):
        for j in range(M):

            # 블록이 층수보다 더 크면
            if map_list[i][j] >= target:
                max_target += map_list[i][j] - target # 블럭제거

            # 블록이 층수보다 더 작으면
            else:
                min_target += target - map_list[i][j] # 블럭추가

    if max_target + B >= min_target: # 제거한 블럭 + 가지고있던 블럭으로 다른 위치에 블럭을 추가할 수 있으면
        # 시간 초를 구하고 최저 시간과 비교 
        if min_target + (max_target * 2) <= ans:
        	# 0부터 256층까지 비교하므로 업데이트 될수록 고층의 최저시간
            ans = min_target + (max_target * 2) # 최저 시간
            idx = target # 층수

print(ans, idx)
