import sys

N = int(sys.stdin.readline())

paper = []
for _ in range(N):
    paper.append(list(map(int,sys.stdin.readline().split())))

ans = [0,0]

def func(x,y,n):
    global ans
    flag = False
    pre_num = paper[y][x]

    if n == 1:
        ans[pre_num] += 1
    else:
        for i in range(n):
            for j in range(1,n):
                if pre_num != paper[y+j][x+i]:
                    flag = False
                    break
                else:
                    flag = True
        
            if sum(paper[y+i][x:x+n]) != pre_num*n or flag == False:
                flag = False
                break
        
        if flag:
            ans[pre_num] += 1
        else:
            next_n = n//2
            func(x, y, next_n)
            func(x , y + next_n, next_n)
            func(x + next_n, y, next_n)
            func(x + next_n, y + next_n, next_n)

func(0,0,N)

print(ans[0])
print(ans[1])

