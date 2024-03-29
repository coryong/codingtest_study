n, l, w, h = map(int, input().split())
first = 0
end = max(l, w, h)

for i in range(100):
    mid = (first + end) / 2
    if (l//mid) * (w//mid) * (h//mid) >= n:
        first = mid
    else:
        end = mid
        
print(first)