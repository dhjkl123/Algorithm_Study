import sys

N = int(sys.stdin.readline())

num_list  = [0] * 10001

for _ in range(N):
    num_list[int(sys.stdin.readline())] += 1

for i,num in enumerate(num_list):
    if num == 0: continue
    else:
        for _ in range(num):
            print(i)
