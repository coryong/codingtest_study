n,m = map(int, input().split())
lst_a = []
lst_b = []

for _ in range(n):
    lst_a.append(list(map(int, input().split())))
                 
for _ in range(m):
    lst_b.append(list(map(int, input().split())) )   
    
if lst_b[0][1] - lst_a[0][1] > 0:
    tmp = lst_b[0][1] - lst_a[0][1]
else:
    tmp = 0    
   
a_idx,a_sum = 0,lst_a[0][0]
b_idx,b_sum = 0,lst_b[0][0]
for i in range(100):
    tmp = max(tmp , lst_b[b_idx][1] - lst_a[a_idx][1])
    
    if i + 1 >= a_sum:
        a_idx += 1
        if a_idx < n:
            a_sum += lst_a[a_idx][0]

    if i + 1 >= b_sum:
        b_idx += 1
        if b_idx < m:
            b_sum += lst_b[b_idx][0]


print(tmp)

