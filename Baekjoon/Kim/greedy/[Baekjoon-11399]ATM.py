N = int(input())
PI = list(map(int, input().split()))

PI.sort()

result = 0 
sum_ = 0 

for P in PI :
    sum_ += P
    result += sum_ 

print(result)

