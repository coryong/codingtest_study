from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split())

adj_list = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M) :
    a, b = map(int, input().split())
    adj_list[a][b] = True 
    adj_list[b][a] = True

visited_bfs = [False] * (N+1)

def bfs(V): 
    q=deque([V])
    visited_bfs[V] = True
    while q :
        V = q.popleft()
        for i in range(1, N+1):
            if not visited_bfs[i] and adj_list[V][i]:
                q.append(i)
                visited_bfs[i] = True

cnt = 0 
for i in range(1, N+1) :
    if not visited_bfs[i]:
        bfs(i)
        cnt += 1

print(cnt)