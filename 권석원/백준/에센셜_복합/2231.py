import sys

def find_gen(num):
    ans = 0
    for n in num:
        ans += int(n)
    return int(num) + ans

gen_list = [0] * 1000001

for i in range(1,1000001):
    num = find_gen(str(i))
    if num < 1000001:
        if gen_list[num] > 0:
            gen_list[num] = min(i,gen_list[num])
        else:
             gen_list[num] = i


num = sys.stdin.readline().rstrip()

print(gen_list[int(num)])
