from collections import deque
def solution(maps):
    answer=0
    leny=len(maps)
    lenx=len(maps[0])
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    q=deque()
    q.append((0,0))
    while q:
        y,x=q.popleft()
        if x==lenx-1 and y==leny-1:
            return maps[y][x]
        for i in range(4):
            newy=y+dy[i]
            newx=x+dx[i]
            if 0<=newy<=leny-1 and 0<=newx<=lenx-1:
                if maps[newy][newx]==1:
                    maps[newy][newx]=maps[y][x]+1
                    q.append((newy,newx))
    return -1