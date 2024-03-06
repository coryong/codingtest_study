from collections import deque
N, W, L = map(int, input().split())

trucks = list(map(int, input().split()))
time = 0 
bridge = deque([0]*W)
trucks = deque(trucks)

while bridge:
    time += 1 

    bridge.popleft()
    if trucks :
        if sum(bridge) + trucks[0] <= L : 
            bridge.append(trucks.popleft())
        
        else :
            bridge.append(0)

print(time)