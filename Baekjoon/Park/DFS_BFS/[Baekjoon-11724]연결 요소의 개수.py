a, b = map(int, input().split())
connect = [[] for _ in range(a + 1)]
check = [False for _ in range(a + 1)]
answer = 0

for _ in range(b):
    c, d = map(int, input().split())
    connect[c].append(d)
    connect[d].append(c)

for i in range(1, a + 1):
    if check[i] == 0:
        stack = [i]
        while stack:
            node = stack.pop()
            if check[node] == False:
                check[node] = True
                for j in connect[node]:
                    if check[j]==False:
                        stack.append(j)
        answer += 1

print(answer)