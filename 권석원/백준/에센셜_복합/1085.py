import sys

x, y, w, h = map(int,sys.stdin.readline().split())

def max_min(a,b):
    return max(a,b) - min(a,b)

min_d = min(x,y,max_min(x,w),max_min(y,h))

print(min_d)