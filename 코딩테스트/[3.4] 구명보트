# 최대 2명인 거 늦게봄;;;
# 투포인터
def solution(people, limit):
    people.sort()
    left = 0
    right = len(people)-1
    cnt = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -=1
        else: # 무거운 사람 한명만 태울 때
            right -=1
        cnt += 1
    
    return cnt
            
