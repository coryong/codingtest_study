def dfs(x):
    global result
    visited[x]=True
    cycle.append(x)
    number=numbers[x]
    if visited[number]:
        if number in cycle:
            print(1,len(cycle))
            print(2,cycle[cycle.index(number):])
            print(cycle)
            result += cycle[cycle.index(number):]
            return
    else:
        dfs(number)

for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N
    result = []
    
    for i in range(1, N+1):
        if not visited[i]:
            cycle = []
            dfs(i)
            
    print(N - len(result))