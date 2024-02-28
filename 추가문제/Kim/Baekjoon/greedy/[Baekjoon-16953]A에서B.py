A, B = map(int, input().split())
cnt = 0

while B >= A :
    tmp = B # 시간 초과를 고려해서  tmp를 둔 후 무한루프에 빠지는것을 방지한다
    if A == B  : 
        print(cnt+1)
        break

    else :
        if B % 2 == 0 : 
            B = B // 2 
            cnt += 1
        
        elif B%10 == 1 : 
            B = B // 10
            cnt += 1
    if tmp == B :
        break    


if B != A :
    print(-1)