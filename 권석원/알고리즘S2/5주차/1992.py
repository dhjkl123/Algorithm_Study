import sys

N = int(sys.stdin.readline())

screen_list = []
ans = ''

for _ in range(N):
    tmp = sys.stdin.readline().rstrip()
    screen_list.append(tmp)

def func(n,x,y):
    global ans
    pixel = screen_list[y][x]
    flag = True

    for i in range(y,y+n):
        if not flag:
            break
        for j in range(x,x+n):
            if pixel != screen_list[i][j]:
                flag = False
                break
            
    
    if not flag:
        ans += '('
        next_n = n//2
        func(next_n, x, y)
        func(next_n, x + next_n, y)
        func(next_n, x, y + next_n)
        func(next_n, x + next_n, y + next_n)
        ans += ')'
    else:
        ans += pixel

func(N,0,0)

print(ans)



