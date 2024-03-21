a=int(input())
x=list(map(int,input().split()))
answer=''
values=list(set(x))
values.sort()
for c in x:
    if answer=='':
        answer=str(values.index(c))
    else:
        answer=answer+' '+str(values.index(c))
print(answer)