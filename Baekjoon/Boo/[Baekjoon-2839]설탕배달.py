N = int(input())
max = N // 3
lst = []
for i in range(max+1):
    j = N - 3*i
    if j % 5 == 0:
        lst.append(i + j//5)
if not lst:
    print(-1)
else:
    print(min(lst))