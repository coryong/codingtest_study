import heapq

n = int(input())
lst = []
kk = list(map(int, input().split()))

for i in kk:
    heapq.heappush(lst, i)
    
for _ in range(1, n):
    ll = list(map(int, input().split()))
    for j in ll:
        heapq.heappush(lst, j)
        heapq.heappop(lst)
        
print(lst[0])