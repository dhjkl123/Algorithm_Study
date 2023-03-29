import sys

def return_line(num, lan_list):
    lines = 0
    for lan in lan_list:
        tmp = lan//num
        if tmp:
            lines += tmp
        else:
            break
    
    return lines


K, N = map(int,sys.stdin.readline().split())

lan_list = []

max_length = 0

for _ in range(K):
    lan = int(sys.stdin.readline())
    lan_list.append(lan)

lan_list.sort(reverse=True)
end = lan_list[0]
start = 1

if K == 1 and N == 1:
    max_length = end
else:
    mid = (start + end)//2

    while start != mid and end != mid:

        lines = return_line(mid,lan_list)
        
        if N > lines: # 더 잘라
            end = mid
            mid = (start + end)//2
        elif N <= lines:
            max_length = max(mid,max_length)
            
            start = mid
            mid = (start + end)//2


    if start == mid:
        lines = return_line(end,lan_list)
        
        if N <= lines:
            max_length = max(end,max_length)
        
        lines = return_line(start,lan_list)
        
        if N <= lines:
            max_length = max(start,max_length)

print(max_length)
    
