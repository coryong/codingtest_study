n, w, L = map(int, input().split())
t = list(map(int, input().split()))

time = 0
b = [0] * w # 다리 상태도 확인할 수 있는 리스트 만들기
    
while b:
    b.pop(0)
    time += 1
    if t:
        if sum(b) + t[0] <= L:
            b.append(t.pop(0))
        else:
            b.append(0)
print(time)
