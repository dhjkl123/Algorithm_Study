import sys

N, M = map(int,sys.stdin.readline().split())

my_dict = dict()

for _ in range(N):
    url, pwd = sys.stdin.readline().rstrip().split()
    my_dict[url] = pwd

for _ in range(M):
    url = sys.stdin.readline().rstrip()
    print(my_dict[url])