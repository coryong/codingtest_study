from collections import deque

def solution(n, edge):
    answer = 0
    graph =[[] for _ in range(n+1)]
    lst = [-1] * (n+1)
    
    for i in edge :
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])  
    
    queue = deque([1])
    lst[1]=0 
    
    while queue :
        now = queue.popleft() 
        
        for i in graph[now]:
            if lst[i] == -1:
                queue.append(i)
                lst[i] = lst[now] + 1 

    for j in lst:
        if j == max(lst):
            answer += 1
    return answer