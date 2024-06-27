import sys
w, n = map(int, sys.stdin.readline().split())
lst = []
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    lst.append([a,b])
lst.sort(key = lambda x : -x[1])
sum = 0
for i in lst:
    if w <= i[0]:
        sum += w *i[1]
        break
    elif w > i[0]:
        w -= i[0]
        sum += i[0] * i[1]
        
print(sum)