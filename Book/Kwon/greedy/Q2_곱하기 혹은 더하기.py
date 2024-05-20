import sys

# 무조건 왼쪽부터 오른쪽으로 계산
# 0과 1 제외하면 모두 곱셈 -> 1보다 작거나 같은 수는 덧셈 아니면 곱셈
def solution(s):
    result = int(s[0])
    
    for i in range(1, len(s)):
        temp = int(s[i])
        if temp <=1 or result <= 1:
            result = temp+result
        else:
            result = temp*result
    
    return result


S = list(sys.stdin.readline().rstrip())
print(solution(S))
