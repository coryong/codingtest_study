n, k = map(int, input().split())
lst = []

for _ in range(n):
    x = int(input())
    lst.append(x)
tmp = -1
cnt = 0
while True:   
    cnt += k // lst[tmp]
    k %= lst[tmp] 
    tmp -= 1
    if k == 0:
        break
print(cnt)