import sys
import heapq


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    max_heap = []
    min_heap = []
    check_list = [False] * N
    pos = 0

    for _ in range(N):
        cmd, num = sys.stdin.readline().split()
        num = int(num)

        if cmd == 'I':
                heapq.heappush(max_heap,(-num, pos))
                heapq.heappush(min_heap,(num, pos))
                check_list[pos] = True
                pos += 1
        else:
            if num > 0:               
                while max_heap and check_list[max_heap[0][1]] == False:
                    heapq.heappop(max_heap)

                if max_heap:
                    _, tmp = heapq.heappop(max_heap)
                    check_list[tmp] = False


            elif num < 0:
                while min_heap and check_list[min_heap[0][1]] == False:
                    heapq.heappop(min_heap)

                if min_heap:
                    _, tmp = heapq.heappop(min_heap)
                    check_list[tmp] = False

    while max_heap and check_list[max_heap[0][1]] == False:
            heapq.heappop(max_heap)
    while min_heap and check_list[min_heap[0][1]] == False:
            heapq.heappop(min_heap)

    
    if min_heap and max_heap:
        print(-max_heap[0][0],min_heap[0][0])
    else:
        print('EMPTY')

