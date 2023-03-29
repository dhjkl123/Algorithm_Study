import sys

N = int(sys.stdin.readline())

num = 666
cnt = 0

while True:
    num_str = str(num)

    if '666' in num_str:
        cnt += 1
    
    if cnt == N:
        print(num)
        break
    
    num += 1
        
