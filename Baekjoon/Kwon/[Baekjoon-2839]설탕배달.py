N = int(input())
cnt = 0
bags = [5, 3]
while N >= 0:
    if N % bags[0] == 0:
        cnt += N // bags[0]
        break
    # 3씩 빼야함
    N -= bags[1]
    cnt += 1

# 조건
result = -1 if N < 0 else cnt
print(result)
