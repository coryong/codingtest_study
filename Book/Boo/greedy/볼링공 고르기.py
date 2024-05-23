n, m = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(len(lst)):
    for j in range(len(lst)):
        if i != j:
            if lst[i] != lst[j]:
                cnt +=1
print(cnt//2)