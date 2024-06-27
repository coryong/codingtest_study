from collections import deque

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
person = []
ans = []
for _ in range(m):
    person.append(list(map(int, input().split())))
    
dx = [1, -1, 0,  0]
dy = [0,  0, 1, -1]

def bfs(x, y, t, lst):
    
    t += 1
    if t == 3:
        lst.append([y,x])
        return lst
    
    for i in range(4):
        x += dx[i]
        y += dy[i]
        if 0<=x<=3 and 0<=y<=3:
            if lst[y,x] != 0:
                tmp = bfs(x,y,t+1,lst)
                ans.append(tmp)
            
        else:
            continue

k = []    
for i in ans:
    aa = []
    for j in i:
        pass
        
        
