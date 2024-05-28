import sys
input = sys.stdin.readline
import heapq as hq
# 메모리 제한 신경써야 함
# 최대힙으로 구현하고 N번째까지 삭제하는 걸로 해야할 듯

n = int(input())
h = []
cnt = 0
for i in range(n):
    temp = list(map(int, input().split()))
    for data in temp:
        if len(h) < n:
            hq.heappush(h, data)
        else:
            if h[0] < data:
                hq.heappop(h)
                hq.heappush(h, data)
print(h[0])
