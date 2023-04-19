import sys

N = int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))

calc =  list(map(int,sys.stdin.readline().split()))
ans_max, ans_min = -1e9, 1e9

def func(idx,p,s,m,d,ans):
    global ans_max, ans_min

    if idx == N-1:
        ans_max = max(ans_max,ans)
        ans_min = min(ans_min,ans)
        return

    if p > 0 : func(idx+1,p-1,s,m,d,ans + A[idx+1])
    if s > 0 : func(idx+1,p,s-1,m,d,ans - A[idx+1])
    if m > 0 : func(idx+1,p,s,m-1,d,ans * A[idx+1])
    if d > 0 : func(idx+1,p,s,m,d-1,ans // A[idx+1] if ans > 0 else (-ans // A[idx+1]) * -1)

func(0,calc[0],calc[1],calc[2],calc[3],A[0])

print(ans_max)
print(ans_min)