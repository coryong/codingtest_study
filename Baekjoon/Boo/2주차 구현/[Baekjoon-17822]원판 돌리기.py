import sys 
from collections import deque 

def spin(arr,t,d):
    if d== 0:
        for _ in range(t):
            arr.appendleft(arr.pop())
    else : 
        for _ in range(t):
            arr.append(arr.popleft())

def check(board,n,m):
    temp_board = [deque([board[i][j] for j in range(m)]) for i in range(n)]
    dx = [0,1] 
    dy = [1,0]
    check = False 
    for i in range(n):
        for j in range(m): 
            for px, py in zip (dx,dy): 
                nx,ny = i+px, (j+py)%m
                if 0<=nx<n and 0<=ny<m and board[i][j] != 0 and board[i][j] == board[nx][ny] : 
                    temp_board[nx][ny] = 0
                    temp_board[i][j] = 0
                    check = True 
    if not check: 
        son = 0 
        mot = 0 
        for i in range(n):
            for j in range(m):
                son += board[i][j]
                if board[i][j] : 
                    mot+=1
        if mot == 0 : 
            return board, False 
        avg = son/mot
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0 : 
                    continue 
                if board[i][j] < avg :
                    temp_board[i][j] += 1 
                elif board[i][j] > avg :
                    temp_board[i][j] -= 1
    return temp_board,True 

if __name__ == "__main__":
    n,m,t = map(int,sys.stdin.readline().split())
    board = [deque(list(map(int,sys.stdin.readline().split()))) for _ in range (n)] 
    command = [list(map(int,sys.stdin.readline().split())) for _ in range(t)]
    for comm in command :  
        #comm[0]의 배수 comm[1] 방향으로 comm[2]칸 회전 
        x,d,k = comm
        for i in range(x,n+1,x):
            spin(board[i-1],k,d)
        board,check_board = check(board,n,m)
        if not check_board : # 숫자가 다 사라짐 
            break 
    
    score =0 
    for b in board:
        score += sum(b)
    print(score)