import sys

line1 = '.' + sys.stdin.readline().rstrip()
line2 = '.' + sys.stdin.readline().rstrip()

len1 = len(line1)
len2 = len(line2) 

d = [[0] * len(line1) for _ in range(len(line2))]

for i in range(1,len1):
    for j in range(1,len2):
        if line1[i] == line2[j]:
            d[j][i] = d[j-1][i-1]+1
        else:
            d[j][i] = max(d[j][i-1],d[j-1][i])

print(d[len2-1][len1-1])

'''
1. dp 테이블 초기 값을 어떻게 해야할지 잘 모르겠음 -> 일단 글자와 맞으면 1 아니면 이전 결과 중 큰 값
2. 중복 글자일때 처리 
ex) ABAABA AA -> 2

'''

# len1 = len(line1)
# len2 = len(line2)

# d = [[0] * len(line1) for _ in range(len(line2))]

# for i in range(len1):
#     for j in range(len2):
#         if i == 0 or j == 0:
#             if i > 0:
#                 d[j][i] = max(d[j][i-1],1 if line1[i] == line2[j] else 0)
#             else:
#                 d[j][i] = 1 if line1[i] == line2[j] else 0
#         else:
#             if line1[i] == line2[j]:
#                 d[j][i] = max(1, d[j-1][i] +1)
#             else:
#                 d[j][i] = max(d[j][i-1],d[j-1][i])

# print(d[len2-1][len1-1])