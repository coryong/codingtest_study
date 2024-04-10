# deque나 list 활용해서도 구현 가능할 듯
# 처음에 O(n^2)로 시간초과 발생
# dict, sliding Window Algorithm을 추가적으로 학습해야 할 듯
# 처음에 문제 해석을 잘못해서 순열까지 건드림
from collections import Counter

s, p = map(int, input().split())
dna = list(input())
A, C, G, T = map(int, input().split())

window = Counter(dna[:p])
cnt = 0

# Counter로 조건 체크
if window['A'] >= A and window['C'] >= C and window['G'] >= G and window['T'] >= T:
    cnt += 1

# 슬라이딩 윈도우 이동
for i in range(p, s):
    # 새로운 원소 추가
    window[string[i]] += 1
    # 왼쪽 원소 제거
    window[string[i - p]] -= 1
    # 현재 구간에서의 조건 체크
    if window['A'] >= A and window['C'] >= C and window['G'] >= G and window['T'] >= T:
        cnt += 1

print(cnt)
