import sys
input = sys.stdin.readline

# 1과 0중에 뭐가 많은지 체크하고
# 연속적으로 뒤집는 수를 센다
def solution(s):
    cnt = 0
    result = 0
    for i in s:
        cnt = cnt + 1 if cnt == '0' else cnt - 1
    # 0이 많은 경우
    if cnt >= 0:
        for i in range(len(s)-1):
            if s[i] == '1' and s[i+1] == '0':
                result += 1
    # 1이 많은 경우
    else:
        for i in range(len(s)-1):
            if s[i] == '0' and s[i+1] == '1':
                result += 1
    
    return result

s = list(input().rstrip())
print(solution(s))
