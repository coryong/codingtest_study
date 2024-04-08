def solution(triangle):
    answer = 0
    cnt = 1
    dp = []
    for i in range(len(triangle)):
        x = []
        for j in range(len(triangle[i])):
            if i == 0:
                x.append(triangle[i][j])
            else:
                if j == 0:
                    x.append(triangle[i][j] + dp[i-1][0])
                elif j == len(triangle[i])-1:
                    x.append(triangle[i][j] + dp[i-1][j-1])
                else:   
                    x.append(triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j]))
                
        dp.append(x)
    
    answer = max(dp[-1])
    return answer 
