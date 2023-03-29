import sys

N = int(sys.stdin.readline())

i = 0
i_sum = 0
pre_nax_num = 1

if N == 1:
    print(1)
else:
    while True:
        i += 1
        i_sum += i
        max_num = 6 * i_sum + 1

        if N > pre_nax_num and N <= max_num:
            print(i+1)
            break
        else:
            pre_nax_num = max_num

