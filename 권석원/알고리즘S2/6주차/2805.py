import sys

N,M = map(int,sys.stdin.readline().split())

tree_list = list(map(int,sys.stdin.readline().split()))

max_tree = max(tree_list)

st,ed = 0, max_tree
mid = (ed+st)//2

while st != mid and ed != mid and ed != st:

    sum_tree = 0

    for tree in tree_list:
        tmp = tree - mid
        if tmp > 0:
            sum_tree += tmp

    if sum_tree < M:
        ed = mid
        mid = (mid+st)//2
    elif sum_tree > M:
        st = mid
        mid = (ed+mid)//2
    else:
        break

print(mid)

