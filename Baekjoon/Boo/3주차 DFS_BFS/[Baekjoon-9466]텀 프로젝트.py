import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(lst, visited, first, cycle):
    global result
    
    visited[first] = True
    x = lst[first]
    cycle.append(first)

    if visited[x]:
        if x in cycle:
            result += cycle[cycle.index(x):]  # 시간초과로 이 부분 구글링해서 참고함
        return
    else:
        dfs(lst, visited, x, cycle)

t = int(input())

for _ in range(t):
    n = int(input())
    result = []
    visited=[False for _ in range(n+1)]
    lst = [0] + list(map(int, input().rstrip().split()))

    for j in range(1, n + 1):  
        
        if not visited[j]:
            cycle = []
            dfs(lst, visited, j, cycle)

    print(n - len(set(result)))  
