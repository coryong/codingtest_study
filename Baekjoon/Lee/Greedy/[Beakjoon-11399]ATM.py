n = int(input())

L=[int(x) for x in input().split()]

L.sort()
hap=0
now=0

for i in L:
    now += i
    hap += now
'''
for x in range(1,n+1):
    hap += sum(L[0:x])
'''
print(hap)
