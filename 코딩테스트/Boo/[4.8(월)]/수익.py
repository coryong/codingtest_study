import sys
input = sys.stdin.readline

while 1 :
    n = int(input())
    if n == 0 :
        break
    lst = list(int(input()) for _ in range(n))  
    for i in range(1, n):
        lst[i] = max(lst[i], lst[i] + lst[i - 1])
    print(max(lst))
    