import sys

n,m = map(int,sys.stdin.readline().split())

rect_list = [[0]*(m+1)]

for i in range(n):
    tmp = ['0'] + list(sys.stdin.readline().rstrip())
    insert_tmp = []
    for j in range(m+1):
        insert_tmp.append(int(tmp[j]))

    rect_list.append(insert_tmp)

ans = 0

for i in range(1,n+1):
    for j in range(1,m+1):
        if rect_list[i][j] == 1:
            rect_list[i][j] = min(rect_list[i][j-1],rect_list[i-1][j],rect_list[i-1][j-1]) + 1
            ans = max(ans,rect_list[i][j])

print(ans**2)

