import sys

N = int(sys.stdin.readline())

g_list = []
d_list = [0] * N

for _ in range(N):
    x, y= map(int,sys.stdin.readline().split())
    g_list.append((x,y))

for a in g_list:
    cnt = 1
    for b in g_list:
        if b[0] > a[0] and b[1] > a[1]:
            cnt +=1
    
    print(cnt,end=' ')
    