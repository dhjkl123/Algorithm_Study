import sys

input_str = sys.stdin.readline().rstrip()

tmp = '(' + input_str
flag = False
num = ''
idx = 0

while True:
    for i in range(idx,len(tmp)):
        if tmp[i] == '-':
            tmp = tmp[:i] + ')-(' + tmp[i+1:]
            idx = i + 2
            break
    
    if i == len(tmp) -1 :
        break


if tmp[-1] != ')':
    tmp += ')'

ans = ''

for t in tmp:
    if t >= '0' and t <= '9':
        num += t
    else:
        if num != '':
            ans += str(int(num))
            num = ''

        ans += t

print(eval(ans))
