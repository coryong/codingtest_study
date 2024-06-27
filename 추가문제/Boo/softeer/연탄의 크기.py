n = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans_lst = []
ans = 1
# for i in range(2,int(lst[-1]**0.5)+2):
for i in range(2,lst[-1]+1):    
    for j in lst:
        if j % i == 0:
            ans = i

    cnt = 0        
    for k in lst:
        if k % ans == 0:
            cnt +=1
    ans_lst.append(cnt)
        
print(max(ans_lst))
            
