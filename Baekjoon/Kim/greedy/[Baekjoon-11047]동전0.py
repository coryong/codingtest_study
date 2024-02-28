from collections import deque
N, K = map(int, input().split())

coin = deque()

for _ in range(N):
    coin.appendleft(int(input()))
cnt = 0 

for c in coin : 
    cnt += K // c 
    K %= c

print(cnt)


# 역정렬을 구하는 방법
# N, K = (map(int,input().split()))
# coin = []
# for i in range(N):
#     coin.append(int(input()))

# count = 0


# for i in reversed(range(N)): # 역정렬 구하는 방법 코드 한줄 줄일수있음
#     if coin[i] <= K :
#         count += (K//coin[i]) 
#         K = K%coin[i]

# print(count)