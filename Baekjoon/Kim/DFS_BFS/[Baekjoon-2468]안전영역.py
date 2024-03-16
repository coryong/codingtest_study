from collections import deque

N = int(input())
graph = []

max_num = 0 

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] > max_num:
            max_num = graph[i][j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b, visited, value) :
    q = deque()
    q.append((a,b))
    visited[a][b] = True

    while q : 
        x,y = q.popleft()

        for i in range(4) :
            nx = x + dx[i] 
            ny = y + dy[i]

            if 0<= nx < N and 0 <= ny < N : 
                if graph[nx][ny] > value and not visited[nx][ny] :
                    q.append((nx, ny))
                    visited[nx][ny] = True

result = 0 
for i in range(max_num):
    visited = [[False] * N for _ in range(N)]
    cnt = 0 

    for j in range(N) :
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == False:
                bfs(j, k, visited, i)
                cnt += 1 

    if cnt > result:
        result = cnt 
    
print(result)