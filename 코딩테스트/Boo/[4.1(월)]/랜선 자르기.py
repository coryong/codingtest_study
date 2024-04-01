import sys

k, n = map(int, sys.stdin.readline().split())
lst = []
for _ in range(k):
    lst.append(int(sys.stdin.readline()))
sum = sum(lst)
s = 1
e = sum // 2
result = 1

while s <= e and s >= 1:
    cnt = 0
    mid = (s + e) // 2
    for i in lst:
        cnt += i // mid
    if cnt < n:
        e = mid -1
    else:
        result = mid
        s = mid + 1
print(result)