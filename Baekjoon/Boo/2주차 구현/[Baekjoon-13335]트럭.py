from collections import deque

n,w,l = map(int,input().split())
lst = list(map(int, input().split()))

q = deque()
cnt = 0
idx = 0

for _ in range(w):
    q.append(0)

while idx < n:
    cnt += 1
    q.popleft()

    if sum(q)+lst[idx] <= l:
        idx += 1
        q.append(lst[idx])
        
    else:
        q.append(0)

while q:
    cnt += 1
    q.popleft()

print(cnt)