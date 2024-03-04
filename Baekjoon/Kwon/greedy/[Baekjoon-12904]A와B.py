# 시간복잡도 생각해야함
# 거꾸로 접근
# pop(), reverse() 따로 봐야함
import sys
S = list(sys.stdin.readlines().rstrip())
T = list(sys.stdin.readlines().rstrip())

flag = False
while len(T) > 0:
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()
    if S == T:
        flag = True
        break

result = 1 if flag == True else 0
print(result)
