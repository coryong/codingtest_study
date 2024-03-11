a,b=list(map(int,input().split()))
answer_list=[]
for _ in range(a):
    answer_list.append(list(map(int,input().split())))
count=int(input())
for _ in range(count):
    x,y,a,b=map(int,input().split())
    answer=0
    for i in range(x-1,a):
        for j in range(y-1,b):
            answer+=answer_list[i][j]
    print(answer)