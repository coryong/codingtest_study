import sys

def solution(N):
    result = 0
    # 3중 for문
    for i in range(N+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    result += 1
    return result


N = int(input())
print(solution(N))
