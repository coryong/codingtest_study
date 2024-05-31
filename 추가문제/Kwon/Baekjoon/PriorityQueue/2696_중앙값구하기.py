import sys
import heapq as hq
input = sys.stdin.readline
# RuntimeError 한번 발생함. -> temp로 리스트와 힙을 계속 만들면 시간복잡도에서 걸림
# 매번 전체 리스트를 슬라이싱하여 새로운 힙을 생성하는 것은 비효율적이며, 특히 리스트가 클 경우 메모리 초과가 발생
# 중간값을 찾을 때, min_heap과 max_heap을 효율적으로 활용하는 것이 중요! -> 실제 코테에서도 충분히 나올 수 있는 내용

import sys
import heapq as hq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m = int(input())
    nums = []
    while len(nums) < m:
        nums.extend(map(int, input().split()))
    
    max_heap = []
    min_heap = []  
    result = []
    
    for i in range(m):
        num = nums[i]
        
        # 최대 힙에 먼저 추가
        if len(max_heap) == 0 or num <= -max_heap[0]:
            hq.heappush(max_heap, -num)
        else:
            hq.heappush(min_heap, num)
        
        # 힙의 크기 조정
        if len(max_heap) > len(min_heap) + 1:
            hq.heappush(min_heap, -hq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            hq.heappush(max_heap, -hq.heappop(min_heap))
        
        # i가 홀수일 때마다 중간값을 추가
        if i % 2 == 0:
            result.append(-max_heap[0])
    
    print(len(result))
    print(*result)



