N, M = map(int, input().split())
x, y, direction = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

visited = [[False]*M for _ in range(N)] # 방문 기록

visited[x][y] = 1 

dx = [0, 0, -1, 1] 
dy = [1, -1, 0, 0]

def turn_left(): 
    global direction
    direction -= 1 
    if direction == -1 :
        direction = 3 

cnt = 1 
turn_time = 0 
while True : 
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if visited[nx][ny] == 0 and maps[nx][ny] == 0 : # 회전 이후 갈 수 있는 칸이 존재할때 
        visited[nx][ny] = 1 
        x = nx 
        y = ny 
        cnt += 1 
        turn_time = 0
        continue

    else :  # 회전 이후 갈 수 없을 때 
        turn_time += 1 
    
    if turn_time == 4 : # 네 방향 모두 갈 수 없을때 뒤로가기
        nx = x - dx[direction]
        ny = y - dy[direction]

        if maps[nx][ny] == 0 : 
            x = nx 
            y = ny 
        else: # 뒤로 갈 수 없는 경우 
            break
        turn_time = 0 
print(cnt)