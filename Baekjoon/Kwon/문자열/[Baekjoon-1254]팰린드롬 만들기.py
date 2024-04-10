# python 슬라이싱을 다시 봐야함.
import sys

def solution(name):
    # 회문이 발생하는지 계속 검사해야함
    # 중앙값을 찾은 후에 좌우 대칭에 맞는 길이를 찾으려다가 생각이 꼬임
    for i in range(len(name)):
        if name[i:] == name[i:][::-1]: # 역순으로 만드는 식(슬라이싱)
            result = len(name) + i
            break
    
    return result

input = sys.stdin.readline
name = list(input().rstrip())
print(solution(name))
