import sys

aprt_list = []

for i in range(15):
    tmp_list = []
    for j in range(15):
        if i == 0:
            tmp_list.append(j+1)
        else:
            num = sum(aprt_list[i-1][:j+1])
            tmp_list.append(num)
    
    aprt_list.append(tmp_list)


T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    print(aprt_list[k][n-1])