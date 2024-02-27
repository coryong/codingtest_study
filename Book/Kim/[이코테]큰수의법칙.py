N, M, K = map(int, input().split())
num = list(map(int, input().split()))
result = 0

num.sort(reverse=True)

first = num[0]
second = num[1]

while True : 

    for i in range(K):
        if M == 0 :
            break

        result += first
        M -= 1

    if M == 0 :
        break
    
    result += second
    M -= 1
    
print(result)
    



