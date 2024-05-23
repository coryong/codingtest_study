import sys
input = sys.stdin.readline

def solution(coins):
    result = 1
    for coin in coins:
        if result < coin:
            break
        result += coin
    
    return result

n = int(input())
coins = sorted(list(map(int, input().split())))
print(solution(coins))
