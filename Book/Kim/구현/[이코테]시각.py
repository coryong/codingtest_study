N = int(input())
cnt = 0
for i in range(N+1): # 시
    for j in range(60) : # 분 
        for k in range(60) : # 초
            if '3' in str(i) + str(j) + str(k) :
                cnt += 1 

print(cnt)