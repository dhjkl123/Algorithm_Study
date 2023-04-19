def solution(N, number):
    answer = 0
    
    d = [set() for i in range(8)]
    
    for i in range(1,8):
        d[i].add(int(str(N)*i))
        for j in range(i//2 +1): # i에다가 j의 경우에서 일어날 수 있는 모든 경우 사칙연산
            for f in d[j]:
                for s in d[i-j]:
                    d[i].add(f+s)
                    d[i].add(f-s)
                    d[i].add(s-f)
                    d[i].add(f*s)
                    if s != 0 : d[i].add(f//s)
                    if f != 0 : d[i].add(s//f)
        if number in d[i]:
            return i
    
    return -1

N, number = map(int,input().split())

print(solution(N,number))