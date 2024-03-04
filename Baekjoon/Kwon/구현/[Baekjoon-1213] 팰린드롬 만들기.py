# collections module을 사용해야 함
# 문장이 홀수든 짝수든 홀수가 2개 이상 나오면 안됨
from collections import Counter
import sys

def solution(name):
    nameCnt = Counter(name)
    oddName = ''
    result = ''

    for i in nameCnt:
        if nameCnt[i] % 2 != 0:
            # 홀수 따로 저장
            oddName += i
            name.remove(i)
    
    if len(oddName) > 1:
        result = "I'm Sorry Hansoo"

    else:
        for i in range(0, len(name), 2):
            result += name[i]
        
        result = (result + oddName + result[::-1])

    return result

name = list(map(str, sys.stdin.readline().rstrip()))
name = sorted(name)
print(solution(name))


