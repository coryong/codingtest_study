a,b=map(int,input().split())
c=list()
count=0
for _ in range(a):
    c.append(int(input()))
i=a-1
while b!=0:
    if b>=c[i]:
        count=count+(b//c[i])
        b=b%c[i]
    else:
        i-=1
print(count)