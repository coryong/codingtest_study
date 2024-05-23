n = int(input())
lst = list(map(int,input().split()))

lst.sort()

cnt = 0
x = 0

for i in lst:
    x += 1
    if x >= i:
        cnt += 1
        x = 0
        
print(cnt)
