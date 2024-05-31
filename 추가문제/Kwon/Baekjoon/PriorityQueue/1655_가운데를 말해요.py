import sys
input = sys.stdin.readline
import heapq as hq

# 시간제한 0.1초 참고
n = int(input())

left = []
right = []

for i in range(n):
    data = int(input())
    # left는 최대힙을, right는 최소힙을 구현해야 함.
    # left에 값을 먼저 넣음
    if len(left) == len(right):
        hq.heappush(left, -data)
    else:
        hq.heappush(right, data)

    #
    if right and -left[0] > right[0]:
        # 서로 값을 바꿔야 함
        l = hq.heappop(left)
        r = hq.heappop(right)

        hq.heappush(right, -l)
        hq.heappush(left, -r)
    
    print(-left[0])
