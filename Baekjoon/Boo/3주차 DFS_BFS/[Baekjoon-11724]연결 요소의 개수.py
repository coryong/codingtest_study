import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
lst = [[] for _ in range(N+1)]
visited = [0]*(N+1)

def bfs(n):
    visited[n] = 1
    q = deque()
    q.append(n)
    while q:
        a = q.popleft()
        for i in lst[a]:
            if not visited[i]:
                visited[i] = visited[a] + 1
                q.append(i)   

for _ in range(M):
    u, v = map(int,sys.stdin.readline().split())
    lst[u].append(v)
    lst[v].append(u)
    
result = 0

for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        result += 1
        
print(result)