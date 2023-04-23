import sys

line_1 = '.' + sys.stdin.readline().rstrip()
line_2 = '.' + sys.stdin.readline().rstrip()

d = [[0] * len(line_1) for _ in range(len(line_2))]
ans = 0

for i in range(1,len(line_2)):
    for j in range(1,len(line_1)):
        if line_2[i] == line_1[j]:
            d[i][j] = d[i-1][j-1] +1
        else:
            d[i][j] = max(d[i][j-1],d[i-1][j])
        
print(d[-1][-1])