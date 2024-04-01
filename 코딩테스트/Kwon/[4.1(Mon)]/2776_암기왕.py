import sys

def solution(note1, note2):
    # Note2가 target
    result = []
    for i in range(len(note2)):
        start = 0
        end = len(note1)-1
        target2 = note2[i]
        flag = False
        while(start <= end):
            mid = (start + end) // 2
            target1 = note1[mid]
            # note2에 해당 값이 있는지 확인
            if target2 == target1:
                flag = True
            # binary Search
            if target2 < note1[mid]:
                end = mid - 1
            else:
                start = mid + 1

        result.append(1 if flag else 0)
    
    return result

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    note1 = sorted(list(map(int, input().split())))
    M = int(input())
    note2 = list(map(int, input().split()))
    result = solution(note1, note2)
    for i in result:
        print(i) 
