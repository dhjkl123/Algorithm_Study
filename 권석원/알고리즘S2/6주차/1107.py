N = int(input())
M = int(input())

brokens = []
if M:
    brokens = input().split()


def check(n):
    strN = str(n)

    for s in strN:
        if s in brokens:
            return False
    return True


res = abs(100-N) # +,- 만 이용해서 채널을 찾을때

for i in range(1000000):
    if check(i):
        res = min(res, len(str(i))+abs(i-N)) 
        # 망가지지 않은 버튼으로 수를 만들 때 누른 횟수 + 그 수에서 +,-로 채널을 찾을 때
        

print(res)