import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())

sadari_dict = dict()
baem_dict = dict()

for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    sadari_dict[x] = y

for _ in range(M):
    u, v = map(int,sys.stdin.readline().split())
    baem_dict[u] = v

game_list = [0] * 101
q = deque()
q.append(1)

while q and 0 in game_list[2:]:
    idx = q.popleft()

    for i in range(idx+1,idx+7): # 현재 위치에서 주사위를 굴려 갈 수 있는 위치
        if i <= 100:
            
            if not game_list[i] or game_list[i] > game_list[idx] +1:
                game_list[i] = game_list[idx] +1

                if i in sadari_dict: # 다음 위치가 사다리로 이동할 수 있을 때
                    sadari = sadari_dict[i]
                    if not game_list[sadari] or game_list[sadari] > game_list[i]:
                        game_list[sadari] = game_list[i]
                        if sadari not in q:
                            q.append(sadari) # 사다리 이동
                elif i in baem_dict: # 다음 위치가 뱀으로 이동할 수 있을 때
                    baem = baem_dict[i]
                    if not game_list[baem] or game_list[baem] > game_list[i]:
                        game_list[baem] = game_list[i]         
                        if baem not in q:
                            q.append(baem) # 뱀 이동
                else:
                    if i not in q:
                        q.append(i) # 다음 위치로

print(game_list[100])
