N = int(input())
candy = [list(input()) for _ in range(N)]

result = 1 

def candy_cnt() :
    max_cnt = 1 

    for i in range(N) :
        cnt = 1 
        for j in range(1, N) :
            if candy[i][j] == candy[i][j-1] : # 가로 확인
                cnt += 1 
            else : 
                cnt = 1 
            max_cnt = max(cnt, max_cnt)

        cnt = 1 
        for j in range(1, N) :
            if candy[j][i] == candy[j-1][i] : # 세로 확인
                cnt += 1 
            else : 
                cnt = 1 
            max_cnt = max(cnt, max_cnt)
    
    return max_cnt


for i in range(N):
    for j in range(N-1) : 
        if j+1 < N and candy[i][j] != candy[i][j+1] :  
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j] # 좌우 swap

            result = max(result, candy_cnt())
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        
        if i+1 < N and candy[i][j] != candy[i+1][j] : 
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j] # 위아래 swap

            result = max(result, candy_cnt())
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

print(result)