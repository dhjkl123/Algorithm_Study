import sys

def func(nums, ans_list, m, k, idx):
    if m == k:
        for ans in ans_list:
            print(ans, end=' ')
        print()
    else:
        for i in range(idx, len(nums)):
            ans_list.append(nums[i])
            func(nums, ans_list, m, k+1, i)
            ans_list.pop()


N, M = map(int,sys.stdin.readline().split())

nums = sorted(list(map(int,sys.stdin.readline().split())))

func(nums, [], M, 0, 0)
