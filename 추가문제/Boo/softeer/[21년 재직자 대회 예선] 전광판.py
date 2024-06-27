t = int(input())

dict = {
    '0' : '1110111',
    '1' : '0010010',
    '2' : '1011101',
    '3' : '1011011',
    '4' : '0111010',
    '5' : '1101011',
    '6' : '1101111',
    '7' : '1110010',
    '8' : '1111111',
    '9' : '1111011',
    '-' : '0000000'
}

for _ in range(t):
    cnt = 0
    a,b = map(str, input().split())
    if len(a) > len(b):
        b = '-' * (len(a) - len(b)) + b
    elif len(a) < len(b):
        a = '-' * (len(b) - len(a)) + a
    for i in range(len(a)):
        n = dict[a[i]]
        m = dict[b[i]]
        for j in range(7):
            if n[j] == '0' and m[j] == '1':
                cnt += 1
            elif n[j] == '1' and m[j] == '0':
                cnt += 1

    print(cnt)