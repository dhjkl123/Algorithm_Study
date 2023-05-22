import sys
from collections import deque

def func_d(num):
    num = int(num)
    num = str(num * 2 % 10000)

    while len(num) < 4:
        num = '0' + num

    return num

def func_s(num):
    num = int(num)

    num -= 1
    if num < 0:
        num = 9999

    num = str(num)

    while len(num) < 4:
        num = '0' + num

    return num

def func_l(num):

    while len(num) < 4:
        num = '0' + num

    return num[1] + num[2] + num[3] + num[0]

def func_r(num): 

    while len(num) < 4:
        num = '0' + num

    return num[3] + num[0] + num[1] + num[2]

def func(num, cmd, tmp, check_list, q):
    num = int(num)
    if len(check_list[num]):
        if len(check_list[num]) > len(tmp + cmd):
            check_list[num] = tmp + cmd
            q.append(str(num))
    else:
        check_list[num] = tmp + cmd
        q.append(str(num))

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int,sys.stdin.readline().split())
    A = str(A)
    B = str(B)

    check_list = [''] * 10000
    q = deque([A])

    while q:
        num = q.popleft()
        tmp = check_list[int(num)]

        if num == B:
            print(tmp)
            break

        num_d = func_d(num)
        func(num_d, 'D', tmp, check_list, q)

        num_s = func_s(num)
        func(num_s, 'S', tmp, check_list, q)

        num_l = func_l(num)
        func(num_l, 'L', tmp, check_list, q)

        num_r = func_r(num)
        func(num_r, 'R', tmp, check_list, q)
