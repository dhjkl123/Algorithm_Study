import sys

N = int(sys.stdin.readline())

num_list = list(map(int,sys.stdin.readline().split()))
d = [0] * N

ans = num_list[0]

for i in range(0,N):
    d[i] = num_list[i]

    for j in range(0,i):
        if num_list[j] < num_list[i]:
            d[i] = max(d[j] + num_list[i], d[i])
 
    ans = max(ans,d[i])

        

print(ans)