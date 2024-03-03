a=int(input())
b=[]
count=0
counta=1
for _ in range(a):
    b.append(list(input()))
for k in range(a):
    counta=1
    for l in range(1,a):
        if b[k][l]==b[k][l-1]:
            counta+=1
        else:
            count=max(count,counta)
            counta=1
    count=max(count,counta)
for k in range(a):
    counta=1
    for l in range(1,a):
        if b[l][k]==b[l-1][k]:
            counta+=1
        else:
            count=max(count,counta)
            counta=1
for i in range(a):
    for j in range(a):
        if j+1<a and b[i][j]!=b[i][j+1] :
            b[i][j],b[i][j+1]=b[i][j+1],b[i][j]
            for k in range(a):
                counta=1
                for l in range(1,a):
                    if b[k][l]==b[k][l-1]:
                        counta+=1
                    else:
                        count=max(count,counta)
                        counta=1
                count=max(count,counta)
            for k in range(a):
                counta=1
                for l in range(1,a):
                    if b[l][k]==b[l-1][k]:
                        counta+=1
                    else:
                        count=max(count,counta)
                        counta=1
                count=max(count,counta)
            #가장 많은 count check
            b[i][j],b[i][j+1]=b[i][j+1],b[i][j]#원상복귀
        if i+1<a and b[i+1][j]!=b[i][j] :
            b[i+1][j],b[i][j]=b[i][j],b[i+1][j]
            for k in range(a):
                counta=1
                for l in range(1,a):
                    if b[k][l]==b[k][l-1]:
                        counta+=1
                    else:
                        count=max(count,counta)
                        counta=1
                count=max(count,counta)
            for k in range(a):
                counta=1
                for l in range(1,a):
                    if b[l][k]==b[l-1][k]:
                        counta+=1
                    else:
                        count=max(count,counta)
                        counta=1
                count=max(count,counta)
            #가장 많은 count check
            b[i+1][j],b[i][j]=b[i][j],b[i+1][j]#원상복귀
print(count)            

        