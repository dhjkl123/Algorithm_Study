import sys

N = int(sys.stdin.readline())
map_list = []

for _ in range(N):
    map_list.append(list(map(int,sys.stdin.readline().split())))

ans = dict()
ans[-1] = 0
ans[0] = 0
ans[1] = 0


def check(arr):
    global ans
    num = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if num != arr[i][j]:
                return False
            
    ans[num] += 1
    return True

def func(x,y,n):

    check_arr = []

    for i in range(y,y+n):
            check_arr.append(map_list[i][x:x+n])

    if check(check_arr):
        return
    else:
        for dy in range(y,y+n,n//3):
            for dx in range(x,x+n,n//3):
                func(dx,dy,n//3)

func(0,0,N)

for key, val in ans.items():
    print(val)