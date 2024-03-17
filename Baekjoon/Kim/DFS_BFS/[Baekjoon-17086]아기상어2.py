from collections import deque
N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]


dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


q = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j]:
            q.append((i,j))

result = 0
while q : 
    x, y = q.popleft()
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M : 
            if not graph[nx][ny] :
                graph[nx][ny] = graph[x][y] + 1 
                result = graph[nx][ny]
                q.append((nx, ny))

print(result-1)
