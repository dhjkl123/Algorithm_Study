import sys
from collections import deque

def func():
    global stack
    print('no')
    stack.clear()
    return True

while True:
    s = sys.stdin.readline().rstrip()

    if s == '.':
        break
    
    stack = deque()
    flag = False

    for a in s:
        if a == '(':
            stack.append(0)
        elif a == '[':
            stack.append(1)

        if a == ')' :
            if stack:
                if stack.pop() != 0:
                    flag = func()
                    break
            else:
                flag = func()
                break

        elif a == ']':
            if stack:
                if stack.pop() != 1:
                    flag = func()
                    break
            else:
                flag = func()
                break
        
    if flag == False and len(stack) == 0:
        print('yes')
    elif stack:
        print('no')

