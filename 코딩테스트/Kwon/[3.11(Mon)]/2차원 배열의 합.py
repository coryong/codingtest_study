# 시간초과
# 부분합
import sys

N, M = list(map(int, sys.stdin.readline().split()))
m = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

K = int(input())

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + m[i-1][j-1] - dp[i-1][j-1]


for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    print(dp[x][y]-dp[x][j-1]-dp[i-1][y]+dp[i-1][j-1])
