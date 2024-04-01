import sys

n = int(sys.stdin.readline())
for _ in range(n):
    k = int(sys.stdin.readline())
    lst1 = list(map(int, sys.stdin.readline().split()))
    l = int(sys.stdin.readline())
    lst2 = list(map(int, sys.stdin.readline().split()))

    result = set(lst1) & set(lst2)
    for i in lst2:
        if i in result:
            print(1)
        else:
            print(0)