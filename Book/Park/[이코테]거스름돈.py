coin=[500,100,50,10]
money=int(input())
i=0
count=0
while money!=0:
   if money>=coin[i]:
       money-=coin[i]
       count+=1
   else:
       i+=1
print(count)