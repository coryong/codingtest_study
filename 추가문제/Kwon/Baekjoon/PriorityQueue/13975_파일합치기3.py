import sys
import heapq as hq
input = sys.stdin.readline

def solution(k, files):
    hq.heapify(files)
    result = 0
    for _ in range(k-1):
        file1 = hq.heappop(files)
        file2 = hq.heappop(files)
        new_file = file1+file2
        result += new_file
        hq.heappush(files, new_file)

    return result

t = int(input())
for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    print(solution(k, files))

