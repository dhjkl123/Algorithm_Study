import sys

T = int(sys.stdin.readline())
answer_list = []
answer_list.append([1,0])
answer_list.append([0,1])

for i in range(2,41):
    zero_cnt_1, one_cnt_1 = answer_list[i-1]
    zero_cnt_2, one_cnt_2 = answer_list[i-2]

    answer_list.append([zero_cnt_1+zero_cnt_2,one_cnt_1+one_cnt_2])

for _ in range(T):
    n = int(sys.stdin.readline())
    z_c, o_c = answer_list[n]

    print(z_c, o_c)
