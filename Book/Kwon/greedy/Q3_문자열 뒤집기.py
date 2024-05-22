import sys
input = sys.stdin.readline

def solution(s):
    cnt0, cnt1 = 0, 0
    if s[0] == '1':
        cnt0 += 1
    else:
        cnt1 += 1
    # 처음에 다르게 계산했다가 바로 오답
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            if s[i+1] == '0':
                cnt1 += 1
            else:
                cnt0 += 1

    return min(cnt0, cnt1)

s = list(input().rstrip())
print(solution(s))
