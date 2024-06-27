import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
lst = [list(sys.stdin.readline()) for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
e = None
s = None
g = []
for i in range(n):
    for j in range(m):
        if lst[i][j] == 'D':
            e = i,j
        elif lst[i][j] == 'G':
            g.append((i,j))
        elif lst[i][j] == 'N':
            s = i,j
if not e or not s:
    print('No')
    exit()
g_minx = 0
g_miny = 0
g_minsum = float('inf')
for k, l in g:
    k = abs(k - e[0])
    l = abs(l - e[1])
    if g_minsum> k+l:
        g_minsum = k+l
        g_minx = k
        g_miny = l

def bfs_m(graph, s,e,n,m):
    q = deque([s])
    visited = [[False]*m for _ in range(n)]
    visited[s[0]][s[1]] = True
    distance = [[float('inf')] * m for _ in range(n)]
    distance[s[0]][s[1]] = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != '#':
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))
                
    return distance

d = bfs_m(lst, s,e,n,m)

if d[e[0]][e[1]] > g_minsum:
    print('No')
else:
    print('Yes')

    