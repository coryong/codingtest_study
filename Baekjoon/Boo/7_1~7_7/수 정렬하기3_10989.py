import sys
input = sys.stdin.readline

n = int(input())
lst = [0] * 10001

for _ in range(n):
    x = int(input())
    lst[x] += 1

for i in range(1, 10001):
    for _ in range(lst[i]):
        sys.stdout.write(f'{i}\n')



# import sys
# input = sys.stdin.readline

# list = [0] * 10001

# for i in range(int(input())):
#     x = int(input().strip())
#     list[x] += 1

# for i in range(1,10001):
#     while list[i] != 0 :
#         sys.stdout.write(str(i) + '\n') 
#         list[i] -= 1