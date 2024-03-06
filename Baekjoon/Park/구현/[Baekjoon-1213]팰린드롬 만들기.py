a=list(input())
a.sort()
answer=[]
counter=[]
solo=0
t=''
for i in a:
    if i not in answer:
        answer.append(i)
        counter.append(int(1))
    else:
        counter[answer.index(i)]+=1
for i in range(len(counter)):
    if counter[i]%2==1:
        solo+=1
        d=answer[i]
    for _ in range(counter[i]//2):
        t+=answer[i]
if solo>1:
    print("I'm Sorry Hansoo")
elif solo==0:
    print(t+t[::-1])
else:
    print(t+d+t[::-1])    
    
