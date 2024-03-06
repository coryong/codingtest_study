import sys

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

while 1:
    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]
    if s == t:
        print('1')
        break
    if len(t) <= 1:
        print('0')
        break