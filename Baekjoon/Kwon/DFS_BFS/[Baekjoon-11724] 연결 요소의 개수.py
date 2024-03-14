import sys
sys.setrecursionlimit(10**6) # 백준의 깊이는 10^3라서 RuntimeError 발생
# 주말에 BFS로 구현해봐야 함.
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def solution(N, M):
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    result = 0
    visited = [False] * (N+1)
    for i in range(1, N+1):
        if not visited[i]:
            dfs(graph, i, visited)
            result += 1

    return result

N, M = map(int, sys.stdin.readline().split())
print(solution(N,M))

