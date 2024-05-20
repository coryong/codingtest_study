import sys

def solution(people):
    cnt = 0
    result = 0

    for person in people:
        cnt += 1
        if cnt >= person: # 와 이렇게 바로바로 생각해야 하는데 잘 안됨.
            result += 1
            cnt = 0
        else:
            continue

    return result


# 오름차순으로 정렬하고 그리디
N = int(input())
people = sorted(list(map(int, sys.stdin.readline().split())))
print(solution(people))
