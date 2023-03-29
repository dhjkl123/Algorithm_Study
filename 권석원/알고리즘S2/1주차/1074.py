import sys

N,r,c = map(int,sys.stdin.readline().split())

def func(n,r,c,y,x,num,real_n):
    if y == r and x == c:
        print(num)
        return
    
    step = pow(2,n)//2

    if y <= r and r < y + step and x <= c and c < x + step: #1st
        func(n-1, r, c, y, x, num, real_n)
    
    elif y <= r and r < y + step and x + step <= c and c < x + step*2: #2nd
        func(n-1, r, c, y, x + step, num + pow(2,2*n-2), real_n) 
    
    elif y + step <= r and r < y + step*2 and x <= c and c < x + step: #3rd
        func(n-1, r, c, y + step, x, num + pow(2,2*n-1), real_n) 
    
    elif y + step <= r and r < y + step*2 and x + step <= c and c < x + step*2: #4th
        func(n-1, r, c, y + step, x + step, num + pow(2,2*n-2) * 3, real_n) 
    
func(N,r,c,0,0,0,pow(2,N))
