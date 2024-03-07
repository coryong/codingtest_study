# queue를 써보자
# 다리 길이와 무게를 신경써야한다
# 한번에 안풀리네
import sys

def solution(L, w, ts):
    bridge = [0]*w # 다리길이만큼 설정
    result = 0
    
    while len(bridge):
        result += 1 # 열차가 끝까지 통과해야 하는 걸 생각해서 얘를 먼저 +1했음.
        # 여기서 생각이 꼬여 시간을 버림
        bridge.pop(0)
        if ts:
            if sum(bridge) + ts[0] <= L:
                bridge.append(ts.pop(0))
            else:
                bridge.append(0)
    
    return result

n, w, L = list(map(int, sys.stdin.readline().split()))
ts = list(map(int, sys.stdin.readline().split()))
print(solution(L, w, ts))
