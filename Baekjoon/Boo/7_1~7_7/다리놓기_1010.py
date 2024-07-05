# T = int(input())

# lst = []
# for i in range(T):
#     N, M = map(int, input().split())
#     result = 1
#     for j in range(N):
#         result = result * (M-j) // (N-j)
        
#     lst.append(int(result))


# for i in range(len(lst)):
#     print(lst[i])

import math

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(bridge)