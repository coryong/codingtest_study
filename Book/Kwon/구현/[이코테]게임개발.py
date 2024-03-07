# brutefoce
# 이미 방문했던 곳은 1으로 바꾸자
# 기차에서 풀어서 주석이 좀 많음
import sys

def solution(x, y, st_d, m):
    result = 1
    m[x][y] = 1 # 첫 장소는 방문처리
    # 북 동 남 서 -> index로 0 1 2 3으로 생각하자.
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    ct_d = st_d # 0 1 2 3
    cnt = 0 # 방향 계산하는 변수
    while True:
        ct_d -= 1
        if ct_d < 0:
            ct_d += 4
        nx = x + dx[ct_d]
        ny = y + dy[ct_d]

        if m[nx][ny] == 0:
            m[nx][ny] = 1
            x = nx
            y = ny
            result += 1
        else: # 바다인 경우
            cnt += 1

        # 바다로 둘러싸인 경우
        if cnt == 4:
            result += 1
            break

    return result


N, M = list(map(int, sys.stdin.readline().split()))
x, y, st_d = list(map(int, sys.stdin.readline().split()))
# 북 동 남 서 [0, 1, 2, 3]
m = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(solution(x, y, st_d, m))
