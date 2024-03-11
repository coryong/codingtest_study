t = int(input())
lst = []

for _ in range(t):
    lst.append(list(input().rstrip()))
    
dx = [0, 1,  0, -1]
dy = [1, 0, -1,  0]

for i in lst:
    x,y = 0, 0
    direction_x, direction_y = 0, 0
    x_lst = [0]
    y_lst = [0]
    result = []
    for j in i:
        if j == 'F':
            x += dx[direction_x]
            y += dy[direction_y]
            x_lst.append(x)
            y_lst.append(y)
        elif j == 'B':
            x -= dx[direction_x]
            y -= dy[direction_y]
            x_lst.append(x)
            y_lst.append(y)
        elif j == 'R':
            direction_x += 1
            direction_y += 1
            if direction_x == 4:
                direction_x = 0 
            if direction_y == 4:
                direction_y = 0  
        elif j == 'L':
            direction_x -= 1
            direction_y -= 1
            if direction_x == -1:
                direction_x = 3
            if direction_y == -1:
                direction_y = 3
    print((max(x_lst) - min(x_lst)) * (max(y_lst) - min(y_lst)))