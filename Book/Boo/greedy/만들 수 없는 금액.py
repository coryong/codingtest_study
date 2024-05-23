n = int(input())
lst = list(map(int, input().split()))
lst.sort()

x = 1
for i in lst:
    if x < i :
        print(x)
        exit()
    x += i
print(x)