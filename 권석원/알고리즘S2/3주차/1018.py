import sys

def toggle(word):
    if word == 'B': return 'W'
    elif word == 'W': return 'B'


def check(y,x):
    pre_word_1 = 'B'
    pre_word_2 = 'W'

    change_1 = 0
    change_2 = 0

    for i in range(8):

        pre_word_1 = toggle(pre_word_1)
        pre_word_2 = toggle(pre_word_2)
    
        for j in range(8):
            
            if pre_word_1 == map_list[y+i][x+j]:
                change_1 += 1
            
            if pre_word_2 == map_list[y+i][x+j]:
                change_2 += 1

            pre_word_1 = toggle(pre_word_1)
            pre_word_2 = toggle(pre_word_2)
    
    return min(change_1,change_2)
            

ans = 1e10

N, M = map(int, sys.stdin.readline().split())

map_list = []

for _ in range(N):
    map_list.append(sys.stdin.readline())

for i in range(N):
    for j in range(M):
        if i + 8 > N or j + 8 > M:
            continue
            
        ans = min(ans,check(i,j))

print(ans)