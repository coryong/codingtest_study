from collections import deque

n, m = map(int, input().split())

lst = []
dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]
q = deque()

def bfs():
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if lst[nx][ny] == 0:
                q.append([nx, ny])
                lst[nx][ny] = lst[x][y] + 1

for i in range(n):
    k = list(map(int, input().split()))
    for j in range(m):
        if k[j] == 1:
            q.append((i, j))
    lst.append(k)

bfs()
result = 0
for i in range(n):
    for j in range(m):
        result = max(lst[i][j], result)

print(result-1)