n=int(input())
ans=sorted(map(int,input().split()))
answer=0
k=0
for i in range(len(ans)):
    answer=answer+int(ans[i])
    k+=answer
print(k)