import sys

T = int(sys.stdin.readline())

for _ in range(T):

    N = int(sys.stdin.readline())
    coins = list(map(int,sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    d = [[0] * (M+1) for _ in range(N)]

    for i in range(N):
        d[i][0] = 1
        for j in range(1, M+1):
            if i-1 >= 0: # 두번째 동전 부터 dp 계산
                if j >= coins[i]:
                    d[i][j] += d[i][j - coins[i]] + d[i-1][j] # 이전 동전이 j를 만드는 경우 + j에서 현재 동전을 빼는 경우의 수
                else:
                    d[i][j] = d[i-1][j]
            else: # 첫번째 동전은 dp 초기값
                if j % coins[i] == 0: # 첫번째 동전으로 만들 수 있는 값만 경우의 수 추가
                    d[i][j] += 1

    
    print(d[N-1][M])

'''
재귀로 풀려고 시도했음
우선 제대로 구현할 수 없었고 분명 시간초과 발생했을 것
'''
# def func(cost,arr,pos):
#     global cnt, M, N

    
#     while cost > 0 and pos < N:
        
#         if cost % arr[pos]: # 해당 동전을 사용해도 돈이 남을 때
#             func(cost % arr[pos],arr,pos+1)
#         else: # 해당 동전을 모두 사용하면 M을 만들 때
#             if pos + 1 != N: 
#                 func(M - cost,arr,pos+1)
#             else:
#                 break
        
#         cost -= arr[pos] #해당 동전을 k 개 사용하는 경우로 계속 넘어감

#     if cost == 0:
#         cnt += 1

#     return