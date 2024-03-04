import sys
N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline().rstrip()) for i in range(N)]

#
cnt = 0
for coin in coins[::-1]:
    if K // coin > 0:
        cnt += K // coin
        K %= coin
    if K <= 0:
        break

print(cnt)

