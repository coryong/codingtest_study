# bruteforce 
# 완탐 문제였는데 오랜만에 풀어서 그런가 코드 진행이 너무 느렸음.
import sys

def solution(N, candies):
    result = 1
    for i in range(N):
        for j in range(N-1):
            # 아래로 검사
            if j+1 < N and candies[i][j] != candies[i][j+1]:
                candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
                result = max(result, checkMax(N, candies))
                # 문제 이해를 잘못해서 원위치로 돌리는걸 몰랐음
                candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
            # 오른쪽 검사
            if i+1 < N and candies[i][j] != candies[i+1][j]:
                candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
                result = max(result, checkMax(N, candies))
                candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
    return result

def checkMax(N, candies):
    maxCnt = 1
    for i in range(N):
        # 가로 탐색 
        cnt = 1
        for j in range(1, N):
            if candies[i][j] == candies[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            maxCnt = max(cnt, maxCnt)
        # 세로 탐색
        cnt = 1
        for j in range(1, N):
            if candies[j][i] == candies[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            maxCnt = max(cnt, maxCnt)
    return maxCnt

N = int(input())
candies = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
print(solution(N, candies))
