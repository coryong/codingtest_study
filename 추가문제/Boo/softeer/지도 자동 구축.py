n = int(input())
tmp = 1
p = 2
for i in range(1,n+1):
    p += tmp
    tmp *= 2
    
    if i == n:
        print(p**2)
        exit()
