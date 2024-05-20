import sys

def solution(coins, k):
    cnt = 0
    # 내림차순
    coins = sorted(coins, reverse=True)
    for coin in coins:
        if k // coin > 0: # coin < k
            cnt += k // coin
            k %= coin
        if k <= 0:
            break

    return cnt


n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline().rstrip()) for i in range(n)]

print(solution(coins, k))
