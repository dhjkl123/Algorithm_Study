import sys

N = int(sys.stdin.readline())

input_list = []

for _ in range(N):
    input_list.append(tuple(map(int,sys.stdin.readline().split())))

input_list.sort(key=lambda x : (x[1],x[0]))

for t in input_list:
    print(t[0],t[1])