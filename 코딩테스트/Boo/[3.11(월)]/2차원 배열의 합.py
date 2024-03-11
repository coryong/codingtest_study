# python3로 제출 시, 시간초과나서
# pypy3로 제출하니까 정답
n, m = map(int, input().split())
lst = []

for _ in range(n):
    lst.append(list(map(int, input().rstrip().split())))

k = int(input())

for _ in range(k):
    result = 0
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            result += lst[i][j]
            
    print(result)
    
# dp 풀이법

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = li[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])