import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    dic = dict()
    for _ in range(N):
        val, key = sys.stdin.readline().rstrip().split()
        if key in dic:
            dic[key].append(val)
        else:
            dic[key] = [val]
    
    ans = 1

    for k,v in dic.items():
        ans *= len(v)+1
    
    print(ans -1)
    