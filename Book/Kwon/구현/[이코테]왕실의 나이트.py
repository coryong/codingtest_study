# ASCII code 잊지말고 기억
import sys

def solution(loc):
    # 나이트 이동 가능 범위
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)]
    #
    x = int(loc[1])
    y = ord(loc[0]) - 96

    # solution
    result = 0
    for move in moves:
        dx = x + move[1]
        dy = y + move[0]
        # 범위 확인
        if dx >= 1 and dy >=1 and dx <= 8 and dy <= 8:
            result += 1 

    return result

loc = input()
print(solution(loc))
