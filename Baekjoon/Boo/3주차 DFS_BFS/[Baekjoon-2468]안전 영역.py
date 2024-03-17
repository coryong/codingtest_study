from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
high = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] > high:
            high = graph[i][j]

dx = [0,0,-1,1]
dy = [-1,1,0,0]
q = deque()

def bfs(i,j, high):
    q.append((i,j))
    visited[i][j] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if graph[nx][ny] > high and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny))

result = 0
for k in range(high):
    visited = [[0] * N for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and visited[i][j] == 0:
                bfs(i,j, k)
                ans += 1
    
    if result < ans:
        result = ans

print(result)