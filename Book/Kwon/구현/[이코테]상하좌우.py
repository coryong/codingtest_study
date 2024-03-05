import sys

def solution(N, moves):
    directions = ['L', 'R', 'U', 'D']
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    x, y = 1, 1
    #
    for move in moves:
        for i in range(len(directions)):
            if move == directions[i]:
                nx = x + dx[i]
                ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > N or ny > N:
                continue
        
        x, y = nx, ny
    return x, y


N = int(input())
moves = list(sys.stdin.readline().split())
print(solution(N, moves))
