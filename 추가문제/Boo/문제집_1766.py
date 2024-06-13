import heapq
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indeg = [0 for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    indeg[b] += 1

heap = []
ans = []
for i in range(1, n+1):
    if indeg[i] == 0:
        heapq.heappush(heap, i)

while heap:
    now = heapq.heappop(heap)
    ans.append(now)

    for node in graph[now]:
        indeg[node] -= 1
        if indeg[node] == 0:
            heapq.heappush(heap, node)
           
print(' '.join(map(str, ans)))