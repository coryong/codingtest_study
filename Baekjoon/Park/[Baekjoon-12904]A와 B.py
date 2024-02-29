a=list(input())
b=list(input())
numa=len(a)
numb=len(b)
while numb>numa:
    if b[numb-1]=="A":
        b.pop()
    else:
        b.pop()
        b=b[::-1]
    numb-=1
if a==b:
    print('1')
else:
    print('0')