N = int(input())
A = list(map(int, input().split()))

# sorting
for i in range(1, N):
    for j in range(i):
        if A[i] < A[j]:
            A[i], A[j] = A[j], A[i]

# 구간 합 배열 생성
result = 0
S = [0] * N 
S[0] = A[0]
for i in range(1, N):
    S[i] = S[i - 1] + A[i]

for i in range(N):
    result += S[i]

print(result)
