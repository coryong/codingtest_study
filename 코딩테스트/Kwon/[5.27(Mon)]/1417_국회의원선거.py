import sys
import heapq

input = sys.stdin.readline

def solution(cds):
    target = cds[0]
    others = [-votes for votes in cds[1:]]
    heapq.heapify(others)
    result = 0

    while others and target <= -others[0]:
        max_votes = -heapq.heappop(others)  
        max_votes -= 1
        target += 1
        result += 1
        heapq.heappush(others, -max_votes)

    return result

n = int(input())
cds = [int(input().strip()) for _ in range(n)]

print(solution(cds))
