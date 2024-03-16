# 최소 칸의 개수를 구하는 문제로
# BFS
# 값을 하나씩 더한다는 생각을 못하고 꼬였다가 책을 보고 알아냄
# 이렇게 풀면 거의 완전탐색아닌가?? 어렵네 DFS BFS
import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
m = [list(map(int, input().rstrip())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    # 상 하 좌 우
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 벗어난 경우
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 괴물인 경우
            if m[nx][ny] == 0:
                continue
            # 1을 방문한 경우
            # 이게 왜 최소지?? 아 ㅇㅇ
            if m[nx][ny] == 1:
                m[nx][ny] = m[x][y]+1
                q.append((nx, ny))

    return m[N-1][M-1]

print(bfs(0,0))
