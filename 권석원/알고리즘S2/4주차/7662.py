import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):

    min_heap = []
    max_heap = []

    N = int(sys.stdin.readline())
    check = []
    idx = 0

    for _ in range(N):
        cmd, num = sys.stdin.readline().split()
        num = int(num)

        if cmd =='I':
            heapq.heappush(min_heap,(num,idx))
            heapq.heappush(max_heap,(-num,idx))
            check.append(True)
            idx += 1
        else:
            if num == 1:
                while max_heap and not check[max_heap[0][1]] :
                    heapq.heappop(max_heap)

                if max_heap:
                    num, idx_tmp = heapq.heappop(max_heap)
                    check[idx_tmp] = False

            else:
                while min_heap and not check[min_heap[0][1]] :
                    heapq.heappop(min_heap)

                if min_heap:
                    num, idx_tmp = heapq.heappop(min_heap)
                    check[idx_tmp] = False

    while max_heap and not check[max_heap[0][1]] :
        heapq.heappop(max_heap)
    
    while min_heap and not check[min_heap[0][1]] :
        heapq.heappop(min_heap)
    
    if min_heap and max_heap:
        print(-max_heap[0][0],min_heap[0][0])
    else:
        print('EMPTY')


