import sys

def solution(sen):
    result = 0
    for i in sen[0].split('+'):
        result += int(i)
    for i in sen[1:]:
        for j in i.split('+'):
            result -= int(j)

    return result


sen = sys.stdin.readline().split('-')
print(solution(sen))
