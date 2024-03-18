from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    # 동 서 남 북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append((0,0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 벗어난 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽이 있는 경우
            if maps[nx][ny] == 0:
                continue
            # 1을 방문한 경우
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y]+1
                q.append((nx, ny))

    result = maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1
    return result
