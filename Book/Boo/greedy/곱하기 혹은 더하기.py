n = input()
x=int(n[0])
for i in range(1,len(n)):
    if int(n[i]) == 0 or int(n[i]) == 1 or x <= 1:
        x += int(n[i])
    else:
        x *= int(n[i])

print(x)