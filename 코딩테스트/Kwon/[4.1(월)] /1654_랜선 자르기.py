# RuntimeError(ZeroDivisionError)
import sys

def solution(K, lines):
    start = 0
    end = max(lines)

    # binary search
    result = 0
    while(start <= end):
        total = 0
        mid = (start+end) // 2
        # ZeroDivisionError 방지
        if mid <= 0:
            return 1
        
        for line in lines:
            # ZeroDivisionError 발생할 수 있음 -> 처리
            total += (line // mid)
        
        if total < K:
            end = mid - 1

        else:
            result = mid
            start = mid + 1

    return result

input = sys.stdin.readline
N, K = map(int, input().split())
lines = [int(input()) for _ in range(N)]
print(solution(K, lines))
