import sys
from math import prod
from itertools import combinations

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    item_dict = dict()
    keys = []

    for _ in range(N):
        item, key = sys.stdin.readline().rstrip().split()

        if key in item_dict :
            item_dict[key].append(item)
        else:
            item_dict[key] = [item]

    for key in item_dict.keys():
        tmp = len(item_dict[key])
        keys.append(tmp)

    ans = 0
    for i, k in enumerate(keys):
        tmp = k*ans + k
        ans += tmp
         
    print(ans)

