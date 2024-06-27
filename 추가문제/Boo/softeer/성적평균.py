import sys

n,k = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

for _ in range(k):
    a,b = map(int, sys.stdin.readline().split())
    print('{:.2f}'.format(sum(lst[a-1:b]) / (b-a+1)))