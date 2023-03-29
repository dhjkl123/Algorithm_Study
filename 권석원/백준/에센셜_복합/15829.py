import sys

L = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()
r = 31
M = 1234567891

ans = 0

for i, s in enumerate(string):
    num = ord(s) - ord('a') +1
    ans += (pow(r,i) * (num))%M

print(ans%M)
