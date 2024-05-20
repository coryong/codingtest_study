import heapq

def solution(pq):
    sum = 0
    while len(pq) > 1:
        data1 = heapq.heappop(pq)
        data2 = heapq.heappop(pq)
        sum += data1 + data2
        heapq.heappush(pq, data1 + data2)

    return sum

N = int(input())
pq = []

for _ in range(N):
    heapq.heappush(pq, int(input()))

print(solution(pq))
