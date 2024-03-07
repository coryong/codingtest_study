x = input().rstrip()
lst = [0 for _ in range(30)] 
result = ''
k = ''
for i in x:
    lst[ord(i)-65] += 1

cnt = 0
for j in range(len(lst)):
    if lst[j] % 2 == 1:
        cnt += 1
        k += chr(j+65)
        
    for _ in range(lst[j]//2):
        result += chr(j+65)
        
if cnt > 1:
	print("I'm Sorry Hansoo")

elif cnt == 0:
	print(result + result[::-1])

else:
	print(result + k + result[::-1])
