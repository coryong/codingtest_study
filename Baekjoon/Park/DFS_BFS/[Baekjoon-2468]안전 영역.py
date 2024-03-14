a=int(input())
square=[[] for _ in range(a)]
for i in range(a):
    square[i].append(map(int,input().split()))