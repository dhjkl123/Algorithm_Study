import sys
import heapq

N = int(sys.stdin.readline())

heap_list = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if heap_list:
            print(heapq.heappop(heap_list)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap_list,[abs(x),x])