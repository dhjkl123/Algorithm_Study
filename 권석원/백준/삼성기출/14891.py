import sys
from collections import deque

chain_list = [[]]

for _ in range(4):
    chain_list.append(deque(list(sys.stdin.readline().rstrip())))

N = int(sys.stdin.readline())

def turn(num,dir,tmp_num):
    global chain_list

    pre_num = num -1 if num > 1 else num
    post_num = num +1 if num < 4 else num

    pre_magnet = chain_list[num][6]
    post_magnet = chain_list[num][2]

    if post_num != num and post_num != tmp_num:
        if post_magnet != chain_list[post_num][6]:
            turn(post_num,dir*-1,num)
    
    if pre_num != num and pre_num != tmp_num:
        if pre_magnet != chain_list[pre_num][2]:
            turn(pre_num,dir*-1,num)

    if dir == 1:
        tmp = chain_list[num].pop()
        chain_list[num].insert(0,tmp)
    else:
        tmp = chain_list[num].popleft()
        chain_list[num].append(tmp)
    
    return

for _ in range(N):
    num, dir = map(int,sys.stdin.readline().split())
    turn(num,dir,0)


ans = 0
S_list = [0,1,2,4,8]

for i in range(1,5):
    ans += S_list[i] if chain_list[i][0] == '1' else 0

print(ans)








