#구성되는 알파벳 파악하기 - Counter
# 홀수인지 짝수인지 체크하기 
# 홀수 개수가 2개 이상이면 팰린드롬이 불가능하다

from collections import Counter

L = list(input())
L.sort()

al = Counter(L) #dic형태로 만들어줌 알아두기

odd =0
target=''
#print(al)
for i in al: # i만하면 key값 al[i] 사용시 value값 
    if al[i] % 2 ==1:
        odd +=1
        target = i
        L.remove(i)

    if odd >1:
        break

if odd >1:
    print("I'm Sorry Hansoo")
else:
    p=''
    for i in range(0,len(L),2):
        p += L[i]
        #print(p)
    print(p + target + p[::-1])
