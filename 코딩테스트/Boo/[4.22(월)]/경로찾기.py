import sys

N = int(sys.stdin.readline().rstrip())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))


lst = []
for i in range(N):
    lst.append(graph[i][:])

def mark_circular(path, i):
    start = path.index(i)
    circular_part = path[start:]
    path.extend(circular_part)
    mark_terminated(path)


def mark_terminated(path):
    for i in range(len(path)):
        for j in range(i+1, len(path)):
            lst[path[i]][path[j]] = 1
        
def dfs(path):
    latest = path[-1]
    is_circular = False
    for i in range(N):
        if graph[latest][i]:
            if i in path:
                mark_circular(path, i)
                return            
            path.append(i)
            dfs(path)
    if not is_circular:
        mark_terminated(path)
            
    
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            dfs([i, j])
for line in lst:
    print(' '.join(map(str, line)))