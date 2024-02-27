N, M = map(int, input().split())
result = 0

for _ in range(N):
    num = list(map(int, input().split()))
    min_ = min(num)
    result = max(result, min_)

print(result)