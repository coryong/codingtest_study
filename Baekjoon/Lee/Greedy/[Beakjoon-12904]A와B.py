#반대로 생각해서 되는지 확인

s = list(input().rstrip())
t = list(input().rstrip())



while len(s) != len(t):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()

if s==t:
    print(1)
else:
    print(0)
