import sys

N, M = map(int,sys.stdin.readline().split())

chess_list = []

for _ in range(N):
    chess_list.append(list(sys.stdin.readline().rstrip()))

pattern_b = list('BWBWBWBW')
pattern_w = list('WBWBWBWB')
pattern_1 = []
pattern_2 = []

for i in range(8):
    if i % 2:
        pattern_1.append(pattern_b)
        pattern_2.append(pattern_w)
    else:
        pattern_1.append(pattern_w)
        pattern_2.append(pattern_b)

def check(x,y):
    cnt_1 = 1e9
    cnt_2 = 1e9

    if x + 8 <= N and y + 8 <= M:
        cnt_1 = 0
        cnt_2 = 0

        for i in range(x,x+8):
            flag_1 = False
            flag_2 = False

            if chess_list[i][y:y+8] != pattern_1[i-x]:
                flag_1 = True
            if chess_list[i][y:y+8] != pattern_2[i-x]:
                flag_2 = True
            
            for k in range(8):
                if flag_1 == False and flag_2 == False:
                    break
                else:
                    if flag_1:
                        if chess_list[i][y+k] != pattern_1[i-x][k]:
                            cnt_1 += 1
                    if flag_2:
                        if chess_list[i][y+k] != pattern_2[i-x][k]:
                            cnt_2 += 1
    
    return min(cnt_1, cnt_2)




ans = 1e9

for i in range(N):
    for j in range(M):
        cnt = check(i,j)
        ans = min(ans,cnt)



print(ans)


                        
                        
