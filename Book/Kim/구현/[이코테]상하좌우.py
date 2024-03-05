N = int(input())
plan = input().split()

x, y = 1, 1 

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for p in plan:
    for i in range(4) :
        if p == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N :  # 벗어나는 경우 무시 
        continue

    x, y = nx, ny

print(x, y)