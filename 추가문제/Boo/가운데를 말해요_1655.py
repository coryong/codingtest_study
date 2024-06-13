# heapq를 하나만 사용하면 X
# 최대힙 최소힙으로 나눠서 풀어야함.

# import heapq
# import sys
# n = int(sys.stdin.readline())

# lst = []

# for _ in range(n):
#     heapq.heappush(lst, sys.stdin.readline())
#     l = len(lst)
#     if l % 2 == 0:
#         print(lst[l // 2 - 1])
#     else:
#         print(min(lst[l // 2]))

import sys
import heapq

n = int(input())
left = []  
right = [] 

for i in range(n):
    x = int(sys.stdin.readline())
    
    if len(left) == 0 or -left[0] >= x:
        heapq.heappush(left, -x)
    else:
        heapq.heappush(right, x)

    if len(left) > len(right) + 1:
        temp = -heapq.heappop(left)
        heapq.heappush(right, temp)
    elif len(right) > len(left):
        temp = heapq.heappop(right)
        heapq.heappush(left, -temp)

    print(-left[0])