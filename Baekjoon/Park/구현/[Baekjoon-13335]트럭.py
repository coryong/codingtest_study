n,w,l=map(int,input().split())
bridge=[0 for _ in range(w)]
trucks=list(map(int,input().split()))
new=trucks.pop(0)
answer=0
count=0
while count<n:
    if sum(bridge)+new<=l:
        a=bridge.pop(0)
        bridge.append(new)
        new=0
        if trucks!=[]:
            new=trucks.pop(0)
        if sum(bridge)!=0:
            answer+=1 # bridge가 모두 0인 경우가 발생해서 그 경우는 배제
        if a!=0:
            count+=1 #count 개수가 트럭 수와 같아야 종료
    else:
        a=bridge.pop(0)
        bridge.append(0)
        if sum(bridge)!=0:
            answer+=1
        if a!=0:
            count+=1
print(answer+1)

#히든케이스 발생(미수정)