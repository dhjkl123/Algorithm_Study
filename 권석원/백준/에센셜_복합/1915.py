
'''
이중for문을 써야한 다는 것
범위로 돌면서 찾아야 한다는 것 까지 생각했지만
점화식을 찾지 못했다.
'''

import sys

n,m = map(int,sys.stdin.readline().split())
arr = []

for _ in range(n):
    line  = sys.stdin.readline().rstrip()
    tmp = []
    for char in line:
        tmp.append(int(char))
    
    arr.append(tmp)

d = [[0] * (m+1) for _ in range(n+1)]
ans = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            d[i+1][j+1] = min(d[i+1][j], d[i][j+1], d[i][j]) + 1
            ans = max(ans, d[i+1][j+1])

print(ans * ans)
