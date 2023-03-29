import sys

time_list = []

N = int(sys.stdin.readline())

for _ in range(N):
    a,b = map(int,sys.stdin.readline().split())
    time_list.append([a,b])

time_list.sort(key=lambda x : x[1])

cnt = 1
i = 0
flag = True

while flag and i+1 < N:
    for j in range(i+1,N):
        if time_list[i][1] <= time_list[j][0]:
            i = j
            cnt += 1
            flag = True
            break
        else:
            flag = False
    
    

print(cnt)


# import sys

# time_list = []

# N = int(sys.stdin.readline())

# for _ in range(N):
#     a,b = map(int,sys.stdin.readline().split())
#     time_list.append([a,b,1])

# time_list.sort()
# ans = 0

# for i in range(N):
#     start,end,cnt = time_list[i]
#     for j in range(i+1,N):
#         s,e,c = time_list[j]
#         if end <= s:
#             time_list[j][2] = max(cnt+1,time_list[j][2])
#             ans = max(ans,time_list[j][2])

# print(ans)

