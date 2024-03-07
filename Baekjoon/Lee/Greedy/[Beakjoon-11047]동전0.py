n,k = map(int,input().split())

L=[]

for _ in range(n):
    L.append(int(input()))

L.sort(reverse=True)

money=0

for i in L:
    if k>= i:
        money += k//i
        k %= i

        if k <= 0:
            break

print(money)
