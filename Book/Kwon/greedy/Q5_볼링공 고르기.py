import sys
input = sys.stdin.readline
from itertools import combinations as cb

def solution(data_cb):
    # 값이 같은 애들만 제외함
    result = 0
    for i in range(len(data_cb)):
        if data_cb[i][0] != data_cb[i][1]:
            result += 1
    
    return result

n, m = map(int, input().split())
data = list(map(int, input().split()))
data_cb = list(cb(data, 2))
print(solution(data_cb))
