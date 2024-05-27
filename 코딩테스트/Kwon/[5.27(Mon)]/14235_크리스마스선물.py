import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
values = []

for i in range(n):
    input_value = list(map(int, input().split()))
    a = input_value[0]

    if a == 0:
        if len(values) <= 0:
            print(-1)
        else:
            temp = hq.heappop(values)
            print(temp[1])
    
    else:
        num, result = input_value[0], input_value[1:]

        for i in range(num):
            hq.heappush(values, (-result[i], result[i]))


