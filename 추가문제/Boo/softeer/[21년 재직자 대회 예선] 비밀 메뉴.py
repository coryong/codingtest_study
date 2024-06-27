m,n,k = map(int, input().split())
menu = input()
user = input()
if menu in user:
    print('secret')
else:
    print('normal')