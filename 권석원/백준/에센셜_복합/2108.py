import sys

N = int(sys.stdin.readline())

num_list = []
sum_num = 0
max_num = -4000
min_num = 4001
nums = [0] * 8001


for i in range(N):
    tmp = int(sys.stdin.readline())

    max_num = max(tmp,max_num)
    min_num = min(tmp,min_num)

    if tmp >= 0:
        nums[tmp] += 1
    else:
        nums[(tmp*-1) + 4000] += 1

    sum_num += tmp

    num_list.append(tmp)

num_list.sort()

print(round(float(sum_num/N)))
print(num_list[(N//2)])

max_val = max(nums)
if nums.count(max_val) > 1:
    idx_list = []
    for i in range(8001):
        if max_val == nums[i]:
            if i > 4000:
                idx_list.append(4000-i)
            else:
                idx_list.append(i)
    idx_list.sort()
    print(idx_list[1])
else:
    ans = nums.index(max_val)
    if ans > 4000:
        print(4000-ans)
    else:
        print(ans)

print(max_num-min_num)