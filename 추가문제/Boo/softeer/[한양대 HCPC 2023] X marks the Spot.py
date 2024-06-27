import math
N = int(input())
lst = []

for _ in range(N):
    lst.append(list(map(str, input().split())))
    
for x,y in lst:
    cnt = 0
    for i in x:
        if i == 'X' or i == 'x':
            break
        cnt +=1
    a = y[cnt]
    if a.isalpha() == True:
        if 97 > ord(a):
            print(a,end='')
        else:
            print(chr(ord(a) - 32),end='')
    else:
        print(a,end='')
