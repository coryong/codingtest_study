N, M, K = map(int, input().split())
num = list(map(int, input().split()))

num.sort(reverse=True)

first = num[0]
second = num[1]

#가장 큰 수가 더해지는 횟쉬
count = int(M/(K+1)) * K # 가장 큰 수가 더해지는 횟수
count += M % (K+1) # 나누어 떨어지지 않았을때 더하는 수

result = 0 
result += (count) * first
result += (M-count) * second

print(result)